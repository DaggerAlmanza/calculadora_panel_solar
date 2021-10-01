# This a file with all object models
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
