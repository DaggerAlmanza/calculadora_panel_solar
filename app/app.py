from flask import Flask, request, render_template, url_for, Response
from core.models import HomeAppliance
import json

app = Flask(__name__)


@app.route("/")
def portada():
    """
    Abrimos nuestra página principal 
    """
    return render_template("datos.html")


@app.route("/Homeappliances", methods=["POST"])
def home_appliances() -> json:
    """
    Recibimos un json con la siguiente estructura:
    {
        "homeAppliances":
        [
            {
                "consumption": 40,
                "consumptions_hour": 3,
                "power_factor_type": 0.85,
                "qty": 3
            }, + dict 
        ]	
    }
    , procesamos la información y devolvemos un json.

    """
    if request.method == "POST":
        home_appliances = request.get_json()
        sum_consumptions: float = 0
        sum_panel: float = 0
        for home_appliance in home_appliances["homeAppliances"]:
            household_appliance = HomeAppliance(**home_appliance)
            sum_consumptions += household_appliance.get_consume()
        sum_panel = (sum_consumptions*1.3)/(
                                    int(home_appliances["solarPanel"])*4)
        print(sum_panel)
    return Response(
        json.dumps({"consumptions": sum_consumptions}),
        mimetype="application/json"
                    )
