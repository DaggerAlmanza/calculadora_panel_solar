import json
import math
from flask import Flask, request, render_template, url_for, Response
from core.models import HomeAppliance


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
    sum_panel: cantidad de paneles solares

    """
    if request.method == "POST":
        home_appliances = request.get_json()
        sum_consumptions: float = 0
        sum_panel: float = 0
        intensity_daily: float = 0
        panels_watt: float = 0
        value_panels = int(home_appliances["solarPanel"])
        for home_appliance in home_appliances["homeAppliances"]:
            household_appliance = HomeAppliance(**home_appliance)
            sum_consumptions += household_appliance.get_consume()

        sum_panel = (sum_consumptions*1.3)/(value_panels*4)
        decimal_part, all_in_one_parte = math.modf(sum_panel)

        if decimal_part >= 0.5:
            sum_panel = all_in_one_parte + 1
        else:
            sum_panel = all_in_one_parte

        intensity_daily = (sum_consumptions/48)
        battery_bank_current = (2*intensity_daily)/0.7
        print(intensity_daily, battery_bank_current)

        panels_watt = sum_panel*value_panels
        print(panels_watt)

    return Response(
        json.dumps({"consumptions": sum_panel}),
        mimetype="application/json"
                    )
