from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config["SECRET_KEY"] = "miclave"


class Formulario(FlaskForm):
    electrodomestico = StringField("Electrodoméstico")
    consumo = StringField("Consumo")
    cantidad = StringField("Cantidad")
    categoria = StringField("Categoría")
    horas = StringField("Horas")
    boton = SubmitField("Enviar")


def form_json(formulario) -> list:
    return [
                {
                    "electrodomestico": formulario.electrodomestico.data,
                    "consumption": formulario.consumo.data,
                    "consumptions_hour": formulario.horas.data,
                    "power_factor_type": formulario.categoria.data,
                    "qty": formulario.cantidad.data
                }
            ]


@app.route("/", methods=["GET", "POST"])
def mensaje():
    formulario = Formulario()
    if formulario.validate_on_submit():
        flash("Gracias por pulsar este botón")
        valores = form_json(formulario)
        return render_template("datos.html", valores=valores)
    return render_template(
        "index.html", formulario=formulario
                          )


# if __name__ == "__main__":
#     app.run(debug=True)
"""
{
            "homeAppliances": [
                {
                    "consumption": formulario.consumo.data,
                    "consumptions_hour": formulario.horas.data,
                    "power_factor_type": formulario.categoria.data,
                    "qty": formulario.cantidad.data
                }
            ]
        }
"""