from providers.osm_provider import OSMProvider


class BusinessService:

    def __init__(self):

        self.provider = OSMProvider()

    def search(self, business, country, state, city):

        return self.provider.search(
            business,
            country,
            state,
            city
        )