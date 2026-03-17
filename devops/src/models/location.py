class Location:
    def __init__(self, id: int, trip_id: int, name: str, country: str):
        self.id = id
        self.trip_id = trip_id
        self.name = name
        self.country = country

    def __repr__(self):
        return f"Location(id={self.id}, trip_id={self.trip_id}, name='{self.name}', country='{self.country}')"