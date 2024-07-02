from dataclasses import dataclass
from datetime import datetime

@dataclass
class Sighting:
    id: int
    datetime: datetime
    city: str
    state: str
    country:str
    shape: str
    duration: int
    duration_hm: str
    comments: str
    date_posted: datetime
    latitude: float
    longitude: float


    def __str__(self):
        return self.country

    def __hash__(self):
        return hash(self.id)