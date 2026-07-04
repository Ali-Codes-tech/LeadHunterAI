from dataclasses import dataclass


@dataclass
class Lead:
    name: str
    rating: str
    reviews: str
    phone: str
    website: str
    score: str