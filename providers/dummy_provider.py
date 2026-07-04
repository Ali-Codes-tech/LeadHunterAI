from providers.base_provider import BaseLeadProvider


class DummyProvider(BaseLeadProvider):

    def search(self, business, country, state, city):

        return [
            {
                "name": "Dallas Auto Center",
                "rating": "3.8",
                "reviews": "18",
                "phone": "+1 555-1111",
                "website": "www.dallasauto.com",
                "score": "92"
            },
            {
                "name": "Texas Car World",
                "rating": "4.1",
                "reviews": "26",
                "phone": "+1 555-2222",
                "website": "www.texascarworld.com",
                "score": "81"
            }
        ]