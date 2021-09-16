# This a file with all object models
from adapters.home_appliances_adapter import HomeAppliancesAdapter


class HomeAppliance(HomeAppliancesAdapter):

    __consumption: int = 0
    __power_factor_types: dict = {
        "A": 0.95,
        "B": 0.90,
        "C": 0.85,
        "D": 0.80,
        "E": 0.75,
        "F": 0.70
    }

    def __init__(
            self,
            consumption: int,
            consumptions_hour: int,
            power_factor_type: str = "A",
            qty: int = 1
            ):
        self.consumptions_hour = consumptions_hour
        self.power_factor_type = power_factor_type.upper()
        self.consumption = consumption
        self.qty = qty

    def __get_power_factor_type__(self, power_factor_type: str) -> float:
        power_factor = self.__power_factor_types.get(power_factor_type)
        return power_factor

    def get_consume(self):
        power_factor = self.__get_power_factor_type__(self.power_factor_type)
        return self.consumption * self.qty / power_factor
