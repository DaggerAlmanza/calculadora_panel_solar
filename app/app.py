from flask import Flask, request, render_template, url_for, Response
from core.models import HomeAppliance
import json

app = Flask(__name__)


@app.route("/")
def portada():
    return render_template("datos.html", sum_consumptions=0)


@app.route('/electrodomesticos', methods=['POST'])
def electrodomesticos():
    if request.method == "POST":
        home_appliances = request.get_json()
        sum_consumptions: float = 0
        for home_appliance in home_appliances["homeAppliances"]:
            household_appliance = HomeAppliance(**home_appliance)
            sum_consumptions += household_appliance.get_consume()
    return Response(json.dumps({"consumptions": sum_consumptions}), mimetype="application/json") 
# jsonify({'Consumo Total': sum_consumptions}) jsonify,
