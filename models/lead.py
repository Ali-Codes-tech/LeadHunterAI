from dataclasses import dataclass
from datetime import datetime


@dataclass
class Lead:
    business_name: str
    category: str
    country: str
    state: str
    city: str

    phone: str = ""
    website: str = ""
    email: str = ""

    rating: float = 0.0
    reviews: int = 0

    score: int = 0

    status: str = "NEW"

    notes: str = ""

    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")