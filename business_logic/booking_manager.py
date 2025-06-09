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

    def create_booking_by_room_type_and_name(
        self, first_name, last_name, email, room_type_description, checkin, checkout
    ):
        # 1. Gast erstellen (oder wiederverwenden, falls vorhanden)
        guest = self.guest_dal.create_guest(first_name, last_name, email)

        # 2. Zimmer mit passendem Typ suchen
        rooms = self.room_dal.read_available_rooms_by_type_and_date(room_type_description, checkin, checkout)
        if not rooms:
            print("Kein verfügbares Zimmer für diese Beschreibung.")
            return None
        room = rooms[0]

        # 3. Preis berechnen (z. B. Nächte × Preis/Nacht)
        nights = (checkout - checkin).days
        price_per_night = room.price_per_night
        total_price = nights * price_per_night

        # 4. Booking-Objekt erstellen
        booking = Booking(
            booking_id=None,
            guest_id=guest.guest_id,
            room_id=room.room_id,
            checkin_date=checkin,
            checkout_date=checkout,
            total_amount=total_price,
            is_cancelled=False
        )

        # 5. In DB speichern
        booking_id = self.booking_dal.create_booking(booking)

        # 6. Booking-Objekt mit ID zurückgeben (optional)
        booking._booking_id = booking_id
        booking.room = room  # für spätere Anzeige im UI
        return booking

    def create_booking(self, guest_id: int, room_id: int, checkin, checkout):
        self.booking_dal.create_booking(guest_id, room_id, checkin, checkout)

    def get_all_bookings_with_hotel_info(self):
        return self.booking_dal.read_all_bookings_with_hotel_info()

    def delete_booking_by_id(self, booking_id: int) -> bool:
        return self.booking_dal.delete_booking_by_id(booking_id)

    def update_phone_number(self, booking_id: int, phone_number: str) -> None:
    # Setzt die Telefonnummer zur Buchung.
        self.__booking_dal.update_phone_number(booking_id, phone_number)

    def get_room_type_booking_stats_by_hotel(self, hotel_id: int) -> dict:
        rows = self.booking_dal.read_bookings_by_hotel_with_room_type(hotel_id)
        stats = {}
        for room_type in rows:
            stats[room_type] = stats.get(room_type, 0) + 1
        return stats

