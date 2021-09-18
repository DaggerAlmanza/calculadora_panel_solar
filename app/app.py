from flask import Flask, request, jsonify, render_template
from core.models import HomeAppliance
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)


class Form(FlaskForm):
    electrodomestico = StringField("Electrodomestico")
    cantidad = StringField("Cantidad")
    categoria = StringField("Categoria")
    enviar = SubmitField("Enviar")


@app.route("/", methods=["GET", "POST"])
def front_end():
    electrodomestico: str = ""
    cantidad: int
    categoria: str
    enviado: bool = False
    formulario = Form()

    if formulario.validate_on_submit():
        enviado = True
        electrodomestico = formulario.electrodomestico.data
        cantidad = formulario.cantidad.data
        categoria = formulario.categoria.data
        formulario.electrodomestico.data = ""
    return render_template(
                            "index.html",
                            electrodomestico=electrodomestico,
                            cantidad=cantidad,
                            categoria=categoria,
                            enviado=enviado,
                            formulario=formulario
                            )


@app.route('/electrodomesticos', methods=['POST'])
def electrodomesticos():
    home_appliances = request.get_json()
    sum_consumptions: float = 0
    for home_appliance in home_appliances["homeAppliances"]:
        household_appliance = HomeAppliance(**home_appliance)
        sum_consumptions += household_appliance.get_consume()

    return jsonify({'Consumo Total': sum_consumptions})
