from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        spaces = []
        for row in rows:
            space = Space(
                row["id"],
                row["user_id"],
                row["space_name"],
                row["space_location"],
                row["space_description"],
                row["price_per_night"],
                row["available_from"],
                row["available_to"]
            )
            spaces.append(space)
        return spaces

    
    def create(self, space):
        self._connection.execute(
            """INSERT INTO spaces
            (user_id, space_name, space_location, space_description, price_per_night, available_from, available_to) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
            [space.user_id, space.space_name, space.space_location, space.space_description, space.price_per_night, space.available_from, space.available_to]
        )

    def find(self, space_id):
        rows = self._connection.execute(
            "SELECT * FROM spaces WHERE id = %s",
            [space_id]
        )
        row = rows[0]
        return Space(
            row["id"],
            row["user_id"],
            row["space_name"],
            row["space_location"],
            row["space_description"],
            row["price_per_night"],
            row["available_from"],
            row["available_to"]
        )
