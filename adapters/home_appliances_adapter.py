import abc


class HomeAppliancesAdapter(abc.ABC):

    @abc.abstractmethod
    def get_consume(self):
        pass
