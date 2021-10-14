import json

from flask import Flask, request, render_template, Response
from core.processors import Calculator
from app.login import hash_email_password, reverse_hash_email_password


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
        email_hash, password_hash = hash_email_password(**login_password)
        print(email_hash, password_hash)
        (reverse_email_hash,
            reverse_password_hash) = reverse_hash_email_password(
                email_hash, password_hash)
        print(reverse_email_hash, reverse_password_hash)

    return render_template("login.html")


@app.route("/homeappliances", methods=["POST"])
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
        calculator_response = Calculator.calculate(home_appliances)

    return Response(
        json.dumps(calculator_response),
        mimetype="application/json"
                    )
