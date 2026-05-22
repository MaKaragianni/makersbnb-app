# class Booking:
#     def __init__(self, id, space_id, space_name, user_id, booking_date, booking_status):
#         self.id = id
#         self.space_id = space_id
#         self.space_name = space_name
#         self.user_id = user_id
#         self.booking_date = booking_date
#         self.booking_status = booking_status

#     def __eq__(self, other):
#         return self.__dict__ == other.__dict__

#     def __repr__(self):
#         return f"Booking({self.id}, {self.space_id}, {self.space_name}, {self.user_id}, {self.booking_date}, {self.booking_status})"

class Booking:
    def __init__(
        self,
        id,
        space_id,
        space_name,
        user_id,
        user_email,
        booking_start,
        booking_end,
        booking_status
    ):
        self.id = id
        self.space_id = space_id
        self.user_id = user_id
        self.user_email = user_email
        self.booking_start = booking_start
        self.booking_end = booking_end
        self.booking_status = booking_status

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Booking({self.id}, {self.space_name}, {self.booking_status})"
