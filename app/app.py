import json

from flask import Flask, request, render_template, Response
from core.processors import Calculator, Login


app = Flask(__name__)


@app.route("/")
def portada():
    """
    Abrimos nuestra página principal 
    """
    return render_template("datos.html")


@app.route("/login", methods=["POST"])
def login() -> json:
    """
    Abrimos nuestra Login
    """
    if request.method == "POST":
        login_password = request.get_json()
        print(login_password)
        response_login = Login().login_email_password(**login_password)
        print(response_login)

    return render_template("login.html")


@app.route("/homeappliances", methods=["POST"])
def home_appliances() -> json:
    """
    Recibimos un json con la siguiente estructura:
    {
        "homeAppliances":
        [
            {
                "homeAppliance": XXX,
                "consumption": 40,
                "consumptions_hour": 3,
                "power_factor_type": 0.85,
                "qty": 3
            }, + ... 
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
        print(home_appliances)
        calculator_response = Calculator.calculate(home_appliances)

    return Response(
        json.dumps(calculator_response),
        mimetype="application/json"
                    )
