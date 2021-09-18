from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
# from flask_wtf.recaptcha import validators
from wtforms import (
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired


app = Flask(__name__)


class Formulario(FlaskForm):
    nombre = StringField('nombre')


@app.route('/')
def informacion():
    return render_template('index.html')
