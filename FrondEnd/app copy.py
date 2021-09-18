from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
# from flask_wtf.recaptcha import validators
from wtforms import (
    StringField,
    BooleanField,
    DateField,
    RadioField,
    SelectField,
    TextField,
    TextAreaField,
    SubmitField,
)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "1.0drV23"


@app.route('/electro')
def informacion():
    return render_template('electro.html')


class Formulario(FlaskForm):
    nombre = StringField('nombre', validators=[DataRequired()])
    edad = BooleanField('Eres mayor de edad')
    sexo = RadioField('Sexo', choices=[('h', 'hombre'),
                                        ('m', 'mujer')])
    color = SelectField('Color favorito:',
                        choices=[('r', 'rojo'), ('v', 'verde'), ('a', 'azul')])
    comentario = TextAreaField()
    boton = SubmitField('Enviar')


@app.route('/index', methods=['GET', 'POST'])
def datos():
    miformulario = Formulario()
    if miformulario.validate_on_submit():
        session['nombre'] = miformulario.nombre.data
        session['edad'] = miformulario.edad.data
        session['sexo'] = miformulario.sexo.data
        session['color'] = miformulario.color.data
        session['comentario'] = miformulario.comentario.data
        return redirect(url_for('electro'))
    return render_template('index.html', formulario=miformulario)
