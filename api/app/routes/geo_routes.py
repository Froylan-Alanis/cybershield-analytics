from pathlib import Path
import pandas as pd
from flask import Blueprint, jsonify, send_file
import json

BASE_DIR = Path(__file__).resolve().parents[3]

ml_file = (
    BASE_DIR
    / "data"
    / "processed"
    / "cybersecurity_ml_ready.parquet"
)

encoders_file = (
    BASE_DIR
    / "data"
    / "metadata"
    / "encoders.json"
)

with open(
    encoders_file,
    encoding="utf-8"
) as f:

    encoders_metadata = json.load(f)

geo_bp = Blueprint(
    "geo",
    __name__
)

geojson_file = (
    BASE_DIR
    / "data"
    / "geojson"
    / "mexico_states.json"
)

@geo_bp.route("/geo/mexico-attacks")
def mexico_attacks():

    df = pd.read_parquet(
        "data/geoparquet/cybersecurity_attacks_geospatial.parquet",
        engine="fastparquet"
    )

    grouped = (
        df.groupby("mexico_state")
        .agg({
            "latitude": "mean",
            "longitude": "mean"
        })
        .reset_index()
    )

    grouped.columns = [
        "state",
        "latitude",
        "longitude"
    ]

    grouped["events"] = (
        df["mexico_state"]
        .value_counts()
        .values
    )

    response = grouped.to_dict(
        orient="records"
    )

    return jsonify(response)

@geo_bp.route("/geo/attacks-by-state")
def attacks_by_state():

    df = pd.read_parquet(
        ml_file,
        engine="fastparquet"
    )

    state_counts = (
    df["mexico_state"]
    .value_counts()
    )

    result = []

    for state_id, attacks in state_counts.items():

        state_name = (
            encoders_metadata["mexico_state"]
            [str(int(state_id))]
        )

        result.append({
            "state": state_name,
            "attacks": int(attacks)
        })

    return jsonify(result)

@geo_bp.route("/geo/mexico-geojson")
def mexico_geojson():

    return send_file(
        geojson_file,
        mimetype="application/json"
    )