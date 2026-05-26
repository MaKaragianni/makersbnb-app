class Space:
    def __init__(self, id, user_id, space_name, space_location, space_description, price_per_night, available_from,  available_to):
        self.id = id
        self.user_id = user_id
        self.space_name = space_name
        self.space_location = space_location
        self.space_description = space_description
        self.price_per_night = price_per_night
        self.available_from = available_from
        self.available_to = available_to

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Space({self.id}, {self.user_id}, { self.space_name}, {self.space_location}, { self.space_description}, {self.price_per_night}, {self.available_from}, {self.available_to})"