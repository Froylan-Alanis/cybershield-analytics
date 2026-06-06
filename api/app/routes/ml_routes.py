from flask import Blueprint, jsonify
import json
from pathlib import Path

ml_bp = Blueprint(
    "ml",
    __name__
)

base_dir = Path(__file__).resolve().parents[3]

metrics_file = (
        base_dir
        / "data"
        / "metrics"
        / "model_metrics.json"
    )


@ml_bp.route("/ml/metrics")
def ml_metrics():

    with open(
        metrics_file,
        "r",
        encoding="utf-8"
    ) as f:
        metrics = json.load(f)

    return jsonify(metrics)

@ml_bp.route("/ml/best-model")
def best_model():

    with open(
        metrics_file,
        encoding="utf-8"
    ) as f:

        metrics = json.load(f)

    best = max(
        metrics.values(),
        key=lambda x: x["accuracy"]
    )

    return jsonify(best)