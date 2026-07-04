from abc import ABC, abstractmethod


class BaseLeadProvider(ABC):

    @abstractmethod
    def search(self, business, country, state, city):
        """
        Return a list of businesses.
        """
        pass