import jwt
from flask import jsonify, request
from config import Config

def verify_request():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Authorization token is missing"}), 401

    try:
        decoded = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        request.user = decoded  # Token verisini request'e ekleyin
        return None
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 403
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 403
