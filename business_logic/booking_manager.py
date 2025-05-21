from datetime import datetime
from data_access.booking_dal import BookingDAL
from model import Booking

class BookingManager:
    def __init__(self):
        self.__booking_dal = BookingDAL()

    def create_booking_if_available(self, guest_id: int, room_no: int, checkin: datetime, checkout: datetime, total_amount: float) -> Booking:
        # Prüft Verfügbarkeit und erstellt Buchung
        if self.__booking_dal.is_room_available(room_no, checkin, checkout):
            return self.__booking_dal.create_new_booking(guest_id, room_no, checkin, checkout, total_amount)
        else:
            raise Exception("Zimmer ist im gewünschten Zeitraum nicht verfügbar.")

    def read_booking(self, booking_id: int) -> Booking | None:
        return self.__booking_dal.read_booking_by_id(booking_id)

    def cancel_booking(self, booking: Booking) -> None:
        # Storniert eine Buchung (is_cancelled setzen)
        booking.cancel()
        self.__booking_dal.update_booking(booking)
