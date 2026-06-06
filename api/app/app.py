from flask import Flask

from routes.analytics_routes import analytics_bp
from routes.geo_routes import geo_bp
from routes.ml_routes import ml_bp
from flask import render_template

app = Flask(__name__)

app.register_blueprint(analytics_bp)
app.register_blueprint(geo_bp)
app.register_blueprint(ml_bp)

@app.route("/")
def home():
    return render_template(
        "dashboard_adminlte.html"
    )

@app.route("/dashboard-adminlte")
def dashboard_adminlte():
    return render_template(
        "dashboard_adminlte.html"
    )

@app.route("/geo-intelligence")
def geo_intelligence():

    return render_template(
        "geo_intelligence.html"
    )

@app.route("/threat-intelligence")
def threat_intelligence():

    return render_template(
        "threat_intelligence.html"
    )

@app.route("/machine-learning")
def machine_learning():

    return render_template(
        "machine_learning.html"
    )

@app.route("/model-evaluation")
def model_evaluation():

    return render_template(
        "model_evaluation.html"
    )

@app.route("/api-monitoring")
def api_monitoring():

    return render_template(
        "api_monitoring.html"
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )