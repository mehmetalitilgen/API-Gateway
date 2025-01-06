from flask import Flask,request ,jsonify

from config import Config

from middlewares.auth import verify_request
from middlewares.logging import log_middleware
from middlewares.rate_limit import setup_rate_limiter
from routes.service_proxy import service_blueprint
from routes.health_check import health_blueprint

app = Flask(__name__)
app.config.from_object(Config)

limiter = setup_rate_limiter(app)


@app.before_request
def before_request():
    if request.path == "/health":
        return None
    auth_response  = verify_request()
    if auth_response:
        return auth_response


@app.after_request
def after_request(response):
    return log_middleware(request,response)


app.register_blueprint(service_blueprint, url_prefix="/api")
app.register_blueprint(health_blueprint)


@app.route("/")
@limiter.limit("5 per minute")
def main():
    return jsonify({"message": "Welcome to the Flask API Gateway!"})

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8080,debug=True)
