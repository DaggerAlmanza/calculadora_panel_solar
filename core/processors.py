# This a file with all object models
import math

from adapters.home_appliances_adapter import HomeAppliancesAdapter
from core.models import HomeAppliances, User, ValueCalculator
from mongoengine.errors import NotUniqueError
from werkzeug.security import generate_password_hash


class HomeAppliance(HomeAppliancesAdapter):

    def __init__(
            self,
            homeAppliance: str,
            consumption: int,
            consumptions_hour: int,
            power_factor_type: float = 0.95,
            qty: int = 1
            ):
        self.homeAppliance = homeAppliance
        self.consumptions_hour = consumptions_hour
        self.power_factor_type = power_factor_type
        self.consumption = consumption
        self.qty = qty

    def __get_power_factor_type__(self, power_factor_type: float) -> float:
        power_factor = power_factor_type
        return power_factor

    def get_consume(self) -> float:
        power_factor = self.__get_power_factor_type__(self.power_factor_type)
        consumption_daily = self.consumption * self.qty / power_factor
        return consumption_daily


class Paneles():

    def __init__(
            self,
            sum_consumptions: float,
            value_panels: int
            ) -> float:

        self.sum_consumptions = sum_consumptions
        self.value_panels = value_panels

    def __panles(
        self,
        sum_consumptions: float,
        value_panels: int
    ) -> float:
        sum_panel = (self.sum_consumptions*1.3)/(self.value_panels*4)
        decimal_part, all_in_one_parte = math.modf(sum_panel)

        if decimal_part >= 0.5:
            sum_panel = all_in_one_parte + 1
        else:
            sum_panel = all_in_one_parte
        return sum_panel

    def get_intensity(self):
        intensity_daily = (self.sum_consumptions/48)
        battery_bank_current = (2*intensity_daily)/0.7
        value_panel = self.__panles(self.sum_consumptions, self.value_panels)
        panels_watt = value_panel*self.value_panels
        return value_panel, panels_watt, battery_bank_current


class Calculator():
    @staticmethod
    def calculate(home_appliances: list):
        sum_consumptions: float = 0
        panels_watt: float = 0
        value_panels = int(home_appliances["solarPanel"])
        for home_appliance in home_appliances["homeAppliances"]:
            household_appliance = HomeAppliance(**home_appliance)
            sum_consumptions += household_appliance.get_consume()
        values_operation = Paneles(sum_consumptions, value_panels)
        (sum_panel,
            panels_watt,
            battery_bank_current) = values_operation.get_intensity()
        response = {
                "panelquantity": sum_panel,
                "batterybank": battery_bank_current,
                "inverterpower": panels_watt
            }
        values_home_appliances = HomeAppliances(
                home_appliances=home_appliances["homeAppliances"])
        values_home_appliances.save()
        values = ValueCalculator(**response)
        values.save()
        return response


class Login():

    def login_email_password(self, email, password):

        password_hash = generate_password_hash(password, method='sha256')
        response = {
                "email": email,
                "password": password_hash
            }
        values_login = User(**response)

        try:
            values_login.save()

        except NotUniqueError:
            return "Usuario existente"
        else:
            return "Exitoso"
