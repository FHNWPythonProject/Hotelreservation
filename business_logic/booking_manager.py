from data_access.booking_dal import BookingDAL

class BookingManager:
    def __init__(self):
        self.booking_dal = BookingDAL()

    def create_booking(self, guest_id: int, room_id: int, checkin, checkout):
        self.booking_dal.create_booking(guest_id, room_id, checkin, checkout)
