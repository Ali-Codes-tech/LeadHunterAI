from providers.dummy_provider import DummyProvider


class BusinessService:

    def __init__(self):
        self.provider = DummyProvider()

    def search(self, business, country, state, city):
        return self.provider.search(
            business,
            country,
            state,
            city
        )