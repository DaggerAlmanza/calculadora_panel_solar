# This a file with all object models
import math
from adapters.home_appliances_adapter import HomeAppliancesAdapter


class HomeAppliance(HomeAppliancesAdapter):

    __consumption: int = 0

    def __init__(
            self,
            consumption: int,
            consumptions_hour: int,
            power_factor_type: float = 0.95,
            qty: int = 1
            ):
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
