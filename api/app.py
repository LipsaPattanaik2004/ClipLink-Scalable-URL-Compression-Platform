from flask import Flask, request, jsonify, redirect
from services.shortener import create_short_url, get_original_url
from services.analytics import get_stats
from services.rate_limiter import is_allowed
from cache.redis_client import redis_client

app = Flask(__name__)

BASE_URL = "http://localhost:5000/"

@app.route("/shorten", methods=["POST"])
def shorten():
    ip = request.remote_addr

    if not is_allowed(ip):
        return jsonify({"error": "Rate limit exceeded"}), 429

    data = request.json
    original_url = data.get("url")

    if not original_url:
        return jsonify({"error": "URL required"}), 400

    short_code = create_short_url(original_url)

    redis_client.set(short_code, original_url)

    return jsonify({
        "short_url": BASE_URL + short_code
    })

@app.route("/<short_code>")
def redirect_url(short_code):
    cached = redis_client.get(short_code)

    if cached:
        return redirect(cached)

    original_url = get_original_url(short_code)

    if not original_url:
        return jsonify({"error": "Not found"}), 404

    redis_client.set(short_code, original_url)

    return redirect(original_url)

@app.route("/stats/<short_code>")
def stats(short_code):
    data = get_stats(short_code)

    if not data:
        return jsonify({"error": "Not found"}), 404

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
