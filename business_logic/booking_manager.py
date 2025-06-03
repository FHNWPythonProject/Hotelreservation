from datetime import datetime
from data_access.booking_dal import BookingDAL
from data_access.guest_dal import GuestDAL
from data_access.room_dal import RoomDAL
from model.booking import Booking
from model.guest import Guest

class BookingManager:
    def __init__(self):
        self.booking_dal = BookingDAL()
        self.guest_dal = GuestDAL()
        self.room_dal = RoomDAL()

    def create_booking_by_room_type_and_name(self, first_name: str, last_name: str, email: str,
                                              room_type_description: str,
                                              checkin: datetime, checkout: datetime) -> Booking | None:
        # Prüfen, ob Gast existiert
        guest = self.guest_dal.read_guest_by_email(email)
        if not guest:
            print(" Gast nicht gefunden – wird neu angelegt.")
            guest = self.guest_dal.create_guest(first_name, last_name, email)

        # Verfügbares Zimmer suchen
        rooms = self.room_dal.read_available_rooms_by_type_and_date(room_type_description, checkin, checkout)
        if not rooms:
            print(" Kein verfügbares Zimmer mit diesem Typ im Zeitraum gefunden.")
            return None

        # Erstes verfügbares Zimmer nehmen
        room = rooms[0]

        # Buchung erstellen
        booking_id = self.booking_dal.create_booking(
            guest_id=guest.guest_id,
            room_id=room.room_id,
            checkin=checkin,
            checkout=checkout
        )

        # Rückgabe als Booking-Objekt
        return Booking(
            booking_id=booking_id,
            guest_id=guest.guest_id,
            room_id=room.room_id,
            checkin_date=checkin,
            checkout_date=checkout,
            is_cancelled=False
        )


    def create_booking(self, guest_id: int, room_id: int, checkin, checkout):
        self.booking_dal.create_booking(guest_id, room_id, checkin, checkout)

    def get_all_bookings_with_hotel_info(self):
        return self.booking_dal.read_all_bookings_with_hotel_info()

    def delete_booking_by_id(self, booking_id: int) -> bool:
        return self.booking_dal.delete_booking_by_id(booking_id)

    def update_phone_number(self, booking_id: int, phone_number: str) -> None:
    # Setzt die Telefonnummer zur Buchung.
        self.__booking_dal.update_phone_number(booking_id, phone_number)
