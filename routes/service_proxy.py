from flask import Blueprint, jsonify, request
from config import Config
from load_balancer.balancer import get_balancer
import requests

service_blueprint = Blueprint("service_blueprint", __name__)
balancer = get_balancer(Config.LOAD_BALANCER_STRATEGY, Config.SERVICE_URLS)

@service_blueprint.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def proxy_service(path):
    try:
        service_url = balancer.get_next_service()
        full_url = f"{service_url}/{path}"
        response = requests.request(
            method=request.method,
            url=full_url,
            json=request.get_json(),
            headers=request.headers,
            timeout=5,
        )
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 503
