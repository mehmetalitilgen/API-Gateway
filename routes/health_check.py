from flask import Blueprint, jsonify

health_blueprint = Blueprint("health_blueprint", __name__)

@health_blueprint.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200
