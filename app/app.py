import json
from flask import Flask, request, render_template, url_for, Response
from core.models import HomeAppliance, Paneles


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
    intensity_daily: corriente diaria, batería de 48 voltios
    battery_bank_current: Banco de batería para la alimentación del inversor (amperios/horas)
    panels_watt: Potencia mínima del inversor en su defecto que sea mucho mayor al valor dado
    """
    if request.method == "POST":
        home_appliances = request.get_json()
        sum_consumptions: float = 0
        panels_watt: float = 0
        value_panels = int(home_appliances["solarPanel"])
        for home_appliance in home_appliances["homeAppliances"]:
            household_appliance = HomeAppliance(**home_appliance)
            sum_consumptions += household_appliance.get_consume()
        values_operation = Paneles(sum_consumptions, value_panels)
        (sum_panel,
            panels_watt,
            battery_bank_current) = values_operation.get_intensity()
        print(sum_panel)

    return Response(
        json.dumps(
            {
                "panelquantity": sum_panel,
                "batterybank": battery_bank_current,
                "inverterpower": panels_watt
            }
                ),
        mimetype="application/json"
                    )
