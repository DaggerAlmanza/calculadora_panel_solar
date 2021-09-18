from flask import Flask, request, jsonify
from core.models import HomeAppliance


app = Flask(__name__)


@app.route('/electrodomesticos', methods=['POST'])
def electrodomesticos():
    home_appliances = request.get_json()
    sum_consumptions: float = 0
    for home_appliance in home_appliances["homeAppliances"]:
        household_appliance = HomeAppliance(**home_appliance)
        sum_consumptions += household_appliance.get_consume()

    return jsonify({'Consumo Total': sum_consumptions})
