from flask import Flask, request, jsonify, render_template, url_for
from core.models import HomeAppliance


app = Flask(__name__)


@app.route("/")
def portada():
    return render_template("datos.html")


@app.route('/electrodomesticos', methods=['POST'])
def electrodomesticos():
    if request.method == "POST":
        home_appliances = request.get_json()
        print(home_appliances)
        sum_consumptions: float = 0
        for home_appliance in home_appliances["homeAppliances"]:
            household_appliance = HomeAppliance(**home_appliance)
            sum_consumptions += household_appliance.get_consume()
        print("valor ", sum_consumptions)
        return render_template("datos.html", sum_consumptions=sum_consumptions)
# jsonify({'Consumo Total': sum_consumptions})
