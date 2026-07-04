import requests

from providers.base_provider import BaseLeadProvider


class OSMProvider(BaseLeadProvider):

    OVERPASS_URL = "https://overpass-api.de/api/interpreter"

    def search(self, business, country, state, city):

        query = f"""
[out:json][timeout:25];

area["name"="{city}"]->.searchArea;

(
  node["shop"="car"](area.searchArea);
  way["shop"="car"](area.searchArea);
);

out center;
"""

        try:

            response = requests.post(
                self.OVERPASS_URL,
                data=query,
                timeout=30
            )

            print("Status Code:", response.status_code)

            if response.status_code != 200:
                print(response.text)
                return []

            data = response.json()

        except Exception as e:
            print("API ERROR:", e)
            return []

        businesses = []

        for element in data.get("elements", []):

            tags = element.get("tags", {})

            businesses.append({

                "name": tags.get("name", "Unknown"),

                "rating": "-",

                "reviews": "-",

                "phone": tags.get("phone", ""),

                "website": tags.get("website", ""),

                "score": "0"

            })

        return businesses