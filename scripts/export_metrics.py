import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

metrics_dir = BASE_DIR / "data" / "metrics"

rf_file = metrics_dir / "random_forest_metrics.json"
xgb_file = metrics_dir / "xgboost_metrics.json"
cat_file = metrics_dir / "catboost_metrics.json"

with open(rf_file, encoding="utf-8") as f:
    rf = json.load(f)

with open(xgb_file, encoding="utf-8") as f:
    xgb = json.load(f)

with open(cat_file, encoding="utf-8") as f:
    cat = json.load(f)

final_metrics = {
    "RandomForest": rf,
    "XGBoost": xgb,
    "CatBoost": cat
}

output_file = metrics_dir / "model_metrics.json"

with open(
    output_file,
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        final_metrics,
        f,
        indent=4
    )

print("Metrics consolidated successfully")
print(output_file)