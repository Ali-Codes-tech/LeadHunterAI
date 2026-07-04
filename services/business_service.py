from providers.provider_manager import ProviderManager


class BusinessService:

    def __init__(self):
        self.provider_manager = ProviderManager()

    def set_provider(self, provider_name):
        self.provider_manager.set_provider(provider_name)

    def search(self, business, country, state, city):

        provider = self.provider_manager.get_provider()

        return provider.search(
            business,
            country,
            state,
            city
        )