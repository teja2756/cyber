"""Minimal local SOC risk dashboard API.

Run locally only. This intentionally contains no authentication or external
network integrations and is not intended for production deployment.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/")
def index():
    return """
    <h1>SOC Risk Scoring Dashboard</h1>
    <p>POST JSON to <code>/score</code> with severity, confidence and exposure from 1-5.</p>
    """

@app.post("/score")
def calculate():
    data = request.get_json(silent=True) or {}
    try:
        severity = int(data["severity"])
        confidence = int(data["confidence"])
        exposure = int(data["exposure"])
        if not all(1 <= x <= 5 for x in (severity, confidence, exposure)):
            raise ValueError
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "severity, confidence and exposure must be integers from 1 to 5"}), 400

    risk = severity * confidence * exposure
    priority = "CRITICAL" if risk >= 81 else "HIGH" if risk >= 51 else "MEDIUM" if risk >= 21 else "LOW"
    return jsonify({"risk_score": risk, "max_score": 125, "priority": priority})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
