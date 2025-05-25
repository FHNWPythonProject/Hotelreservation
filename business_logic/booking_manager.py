from data_access.booking_dal import BookingDAL

class BookingManager:
    def __init__(self):
        self.booking_dal = BookingDAL()

    def create_booking(self, guest_id: int, room_id: int, checkin, checkout):
        self.booking_dal.create_booking(guest_id, room_id, checkin, checkout)

    def get_all_bookings_with_hotel_info(self):
        return self.booking_dal.read_all_bookings_with_hotel_info()

    def update_phone_number(self, booking_id: int, phone_number: str) -> None:
    # Setzt die Telefonnummer zur Buchung.
        self.__booking_dal.update_phone_number(booking_id, phone_number)
