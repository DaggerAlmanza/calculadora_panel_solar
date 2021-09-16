from flask import Flask, request, jsonify
from core.models import HomeAppliance

app = Flask(__name__)


@app.route('/electrodomesticos', methods=['POST'])
def electrodomesticos():
    data = request.get_json()
    for iter_number in range(len(data["homeAppliaces"])):
        household_appliance = HomeAppliance(
                            **data["homeAppliaces"][iter_number])
        sum_consumptions = household_appliance.get_consume()

    return jsonify({'Consumo Total': sum_consumptions})
