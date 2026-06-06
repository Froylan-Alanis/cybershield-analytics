from flask import Blueprint, jsonify
import pandas as pd
from pathlib import Path
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
    "r",
    encoding="utf-8"
) as f:

    encoders_metadata = json.load(f)

analytics_bp = Blueprint(
    "analytics",
    __name__
)

@analytics_bp.route("/analytics/summary")
def analytics_summary():

    df = pd.read_parquet(
    ml_file,
    engine="fastparquet"
)

    response = {
        "total_records": len(df),
        "total_features": len(df.columns),
        "attack_distribution":
            df["attack_type"]
            .value_counts()
            .to_dict()
    }

    return jsonify(response)

@analytics_bp.route("/analytics/kpis")
def analytics_kpis():

    df = pd.read_parquet(
    ml_file,
    engine="fastparquet"
)

    response = {

        "total_attacks": len(df),

        "ddos_attacks":
            int(
                (df["attack_type"] == 0).sum()
            ),

        "malware_attacks":
            int(
                (df["attack_type"] == 1).sum()
            ),

        "intrusion_attacks":
            int(
                (df["attack_type"] == 2).sum()
            ),

        "best_model":
            "Random Forest"
    }

    return jsonify(response)

@analytics_bp.route("/analytics/executive-kpis")
def executive_kpis():

    df = pd.read_parquet(
        ml_file,
        engine="fastparquet"
    )

    top_state = (
        df["mexico_state"]
        .value_counts()
        .idxmax()
    )

    top_attack = (
        df["attack_type"]
        .value_counts()
        .idxmax()
    )

    dominant_severity = (
        df["severity_level"]
        .value_counts()
        .idxmax()
    )

    avg_anomaly_score = round(
        df["anomaly_scores"].mean(),
        2
    )

    top_state_name = (
    encoders_metadata["mexico_state"]
    [str(int(top_state))]
    )

    top_attack_name = (
    encoders_metadata["attack_type"]
    [str(int(top_attack))]
    )

    severity_name = (
    encoders_metadata["severity_level"]
    [str(int(dominant_severity))]
    )

    response = {

    "total_attacks":
        len(df),

    "top_state":
        top_state_name,

    "top_attack_type":
        top_attack_name,

    "dominant_severity":
        severity_name,

    "avg_anomaly_score":
        avg_anomaly_score
    }

    return jsonify(response)

@analytics_bp.route("/analytics/state-distribution")
def state_distribution():

    df = pd.read_parquet(
        ml_file,
        engine="fastparquet"
    )

    state_counts = (
        df["mexico_state"]
        .value_counts()
        .sort_values(
            ascending=False
        )
    )

    result = []

    for state_id, count in state_counts.items():

        state_name = (
            encoders_metadata["mexico_state"]
            [str(int(state_id))]
        )

        result.append({
            "state": state_name,
            "attacks": int(count)
        })

    return jsonify(result)

@analytics_bp.route("/analytics/events")
def analytics_events():

    df = pd.read_parquet(
        ml_file,
        engine="fastparquet"
    )

    events = df.head(100).copy()

    result = []

    for _, row in events.iterrows():

        result.append({

            "attack_type":
                encoders_metadata["attack_type"][
                    str(int(row["attack_type"]))
                ],

            "severity_level":
                encoders_metadata["severity_level"][
                    str(int(row["severity_level"]))
                ],

            "state":
                encoders_metadata["mexico_state"][
                    str(int(row["mexico_state"]))
                ],

            "protocol":
                encoders_metadata["protocol"][
                    str(int(row["protocol"]))
                ],

            "traffic_type":
                encoders_metadata["traffic_type"][
                    str(int(row["traffic_type"]))
                ],

            "network_segment":
                encoders_metadata["network_segment"][
                    str(int(row["network_segment"]))
                ],

            "anomaly_score":
                round(
                    float(
                        row["anomaly_scores"]
                    ),
                    2
                )

        })

    return jsonify(result)

@analytics_bp.route("/threat/overview")
def threat_overview():

    df = pd.read_parquet(
        ml_file,
        engine="fastparquet"
    )

    attack_types = (
        df["attack_type"]
        .value_counts()
        .to_dict()
    )

    severity = (
        df["severity_level"]
        .value_counts()
        .to_dict()
    )

    protocols = (
        df["protocol"]
        .value_counts()
        .to_dict()
    )

    traffic_types = (
        df["traffic_type"]
        .value_counts()
        .to_dict()
    )

    segments = (
        df["network_segment"]
        .value_counts()
        .to_dict()
    )

    attack_types = {

        encoders_metadata["attack_type"][str(k)]:
        int(v)

        for k, v in attack_types.items()

    }

    severity = {

        encoders_metadata["severity_level"][str(k)]:
        int(v)

        for k, v in severity.items()

    }

    protocols = {

        encoders_metadata["protocol"][str(k)]:
        int(v)

        for k, v in protocols.items()

    }

    traffic_types = {

        encoders_metadata["traffic_type"][str(k)]:
        int(v)

        for k, v in traffic_types.items()

    }

    segments = {

        encoders_metadata["network_segment"][str(k)]:
        int(v)

        for k, v in segments.items()

    }

    response = {

        "attack_types": attack_types,
        "severity": severity,
        "protocols": protocols,
        "traffic_types": traffic_types,
        "segments": segments

    }

    return jsonify(response)

@analytics_bp.route("/api/status")
def api_status():

    response = [

        {
            "endpoint":
                "/analytics/executive-kpis",

            "status":
                "Online"
        },

        {
            "endpoint":
                "/threat/overview",

            "status":
                "Online"
        },

        {
            "endpoint":
                "/geo/attacks-by-state",

            "status":
                "Online"
        },

        {
            "endpoint":
                "/ml/metrics",

            "status":
                "Online"
        },

        {
            "endpoint":
                "/ml/best-model",

            "status":
                "Online"
        }

    ]

    return jsonify(response)