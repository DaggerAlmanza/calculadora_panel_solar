from mongoengine import Document, StringField, IntField, FloatField,\
    connect, EmbeddedDocumentListField, EmbeddedDocument


connect(host="mongodb://dgadmin:r1e5o6c7eDr9Gg.Lel@127.0.0.1:27017/calculator")


class HomeAppliance(EmbeddedDocument):
    consumption = IntField(required=True)
    consumptions_hour = IntField(required=True)
    power_factor_type = FloatField(required=True)
    qty = IntField(required=True)
    home_appliances = StringField(default="TV")


class HomeAppliances(Document):
    home_appliances = EmbeddedDocumentListField(HomeAppliance)


class ValueCalculator(Document):
    panelquantity = IntField(required=True)
    batterybank = FloatField(required=True)
    inverterpower = FloatField(requiter=True)
