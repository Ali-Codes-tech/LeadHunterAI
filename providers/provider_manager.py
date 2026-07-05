from providers.dummy_provider import DummyProvider


class ProviderManager:

    def __init__(self):
        self.providers = {
            "Dummy": DummyProvider(),
        }

        self.current_provider = "Dummy"

    def get_provider(self):
        return self.providers[self.current_provider]

    def set_provider(self, provider_name):
        if provider_name in self.providers:
            self.current_provider = provider_name