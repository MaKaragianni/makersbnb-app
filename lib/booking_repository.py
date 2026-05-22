from lib.booking import Booking

# class BookingRepository:
#     def __init__(self, connection):
#         self._connection = connection

#     def all(self):
#         rows = self._connection.execute("SELECT * FROM bookings")

#         bookings = []

#         for row in rows:
#             booking = Booking(
#                 row["id"],
#                 row["space_id"],
#                 None,
#                 row["user_id"],
#                 #row["booking_date"],
#                 row["booking_start"],
#                 row["booking_end"],
#                 row["booking_status"]
#             )
#             bookings.append(booking)
#         return bookings

    # def create(self, booking):
    #     self._connection.execute(
    #         """
    #         INSERT INTO bookings   
    #         (space_id, user_id, booking_date, booking_status) VALUES (%s, %s, %s, %s)
    #         """,
    #         [booking.space_id, booking.user_id, booking.booking_date, booking.booking_status]
    #     )

    # def find_by_user_id(self, user_id):
    #     rows = self._connection.execute(
    #         """SELECT bookings.*, spaces.space_name 
    #         FROM bookings 
    #         JOIN spaces ON bookings.space_id = spaces.id 
    #         WHERE bookings.user_id = %s""", 
    #         [user_id]
    #         )
    #     bookings = []
    #     for row in rows:
    #         booking = Booking(
    #             row["id"],
    #             row["space_id"],
    #             row["user_id"],
    #             row["booking_date"],
    #             row["booking_status"]                
    #         )
    #         bookings.append(booking)
    #     return bookings
    
    # def find_by_space_owner(self, owner_user_id):
    #     rows = self._connection.execute(
    #         """SELECT bookings.*, spaces.name ON space_name, users.name ON user_name
    #         FROM bookings 
    #         JOIN spaces ON bookings.space_id = spaces.id 
    #         JOIN users ON bookings.user_id = users.id
    #         WHERE spaces.user_id = %s""", 
    #         [owner_user_id]
    #         )
    #     bookings = []
    #     for row in rows:
    #         booking = Booking(
    #             row["id"],
    #             row["space_name"],
    #             row["space_id"],
    #             row["user_id"],
    #             row["user_name"],
    #             row["booking_date"],
    #             row["booking_status"]                
    #         )
    #         bookings.append(booking)
    #     return bookings


class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, booking):

        self._connection.execute(
            """
            INSERT INTO bookings
            (space_id, user_id, booking_start, booking_end, booking_status)
            VALUES (%s, %s, %s, %s, %s)
            """,
            [
                booking.space_id,
                booking.user_id,
                booking.booking_start,
                booking.booking_end,
                booking.booking_status
            ]
        )

    def find_by_user_id(self, user_id):
            rows = self._connection.execute(
                """SELECT bookings.*, spaces.space_name 
                FROM bookings 
                JOIN spaces ON bookings.space_id = spaces.id 
                WHERE bookings.user_id = %s""", 
                [user_id]
            )
            bookings = []
            for row in rows:
                booking = Booking(
                    row["id"],
                    row["space_id"],
                    row["user_id"],
                    row["booking_start"],
                    row["booking_end"],
                    row["booking_status"]
                )
                booking.space_name = row["space_name"]
                bookings.append(booking)
            return bookings
    
    def find_by_space_owner(self, owner_user_id):
        rows = self._connection.execute(
            """SELECT bookings.*, spaces.space_name 
            FROM bookings 
            JOIN spaces ON bookings.space_id = spaces.id 
            WHERE spaces.user_id = %s""", 
            [owner_user_id]
        )
        bookings = []
        for row in rows:
            booking = Booking(
                row["id"],
                row["space_id"],
                row["user_id"],
                row["booking_start"],
                row["booking_end"],
                row["booking_status"]
            )
            booking.space_name = row["space_name"]
            bookings.append(booking)
        return bookings    

    def booking_requests_made(self, user_id):

        rows = self._connection.execute(
            """
            SELECT bookings.*, spaces.space_name, users.email
            FROM bookings
            JOIN spaces ON bookings.space_id = spaces.id
            JOIN users ON bookings.user_id = users.id
            WHERE bookings.user_id = %s
            """,
            [user_id]
        )

        bookings = []

        for row in rows:

            booking = Booking(
                row["id"],
                row["space_id"],
                row["space_name"],
                row["user_id"],
                row["email"],
                row["booking_start"],
                row["booking_end"],
                row["booking_status"]
            )

            bookings.append(booking)

        return bookings

    def booking_requests_received(self, owner_user_id):

        rows = self._connection.execute(
            """
            SELECT bookings.*, spaces.space_name, users.email
            FROM bookings
            JOIN spaces ON bookings.space_id = spaces.id
            JOIN users ON bookings.user_id = users.id
            WHERE spaces.user_id = %s
            """,
            [owner_user_id]
        )

        bookings = []

        for row in rows:

            booking = Booking(
                row["id"],
                row["space_id"],
                row["space_name"],
                row["user_id"],
                row["email"],
                row["booking_start"],
                row["booking_end"],
                row["booking_status"]
            )

            bookings.append(booking)

        return bookings

    def update_status(self, booking_id, status):

        self._connection.execute(
            """
            UPDATE bookings
            SET booking_status = %s
            WHERE id = %s
            """,
            [status, booking_id]
        )