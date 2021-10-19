import os
from mongoengine import Document, StringField, IntField, FloatField,\
    connect, EmbeddedDocumentListField, EmbeddedDocument


connect(host="mongodb://dgadmin:r1e5o6c7eDr9Gg.Lel@127.0.0.1:27017/calculator")


class HomeAppliance(EmbeddedDocument):
    homeAppliance = StringField(default="TV")
    consumption = IntField(required=True)
    consumptions_hour = IntField(required=True)
    power_factor_type = FloatField(required=True)
    qty = IntField(required=True)


class HomeAppliances(Document):
    home_appliances = EmbeddedDocumentListField(HomeAppliance)


class ValueCalculator(Document):
    panelquantity = IntField(required=True)
    batterybank = FloatField(required=True)
    inverterpower = FloatField(requiter=True)


class User(Document):
    email = StringField(required=True, unique=True)
    password = StringField(required=True)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or\
        b'\xa5\x8b.\x95}\xc9\xcf\xfc\xe3&\x8f,3\xf1\x9cd'
