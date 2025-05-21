from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.hotel import Hotel
    from model.room_type import RoomType
    from model.booking import Booking


class Room:
    def __init__(self, room_id, room_number, price_per_night, max_guests, hotel_id, room_type):
        self.room_id = room_id
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.hotel_id = hotel_id
        self.room_type = room_type


    def __repr__(self):
        # kurze Textdarstellung des Zimmers
        return f"Room(no={self.__room_no}, price={self.__price_per_night})"

    @property
    def room_no(self) -> int:
        return self.__room_no

    @property
    def price_per_night(self) -> float:
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, price: float):
        # setzt neuen Zimmerpreis, muss gültig sein
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("price must be a positive number")
        self.__price_per_night = price

    @property
    def hotel(self) -> Hotel:
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel: Hotel):
        from model import Hotel
        if hotel is not None and not isinstance(hotel, Hotel):
            raise ValueError("hotel must be an instance of Hotel")
        self.__hotel = hotel

    @property
    def room_type(self) -> RoomType:
        return self.__room_type

    @room_type.setter
    def room_type(self, room_type: RoomType):
        from model import RoomType
        if room_type is not None and not isinstance(room_type, RoomType):
            raise ValueError("room_type must be an instance of RoomType")
        self.__room_type = room_type

    @property
    def bookings(self) -> list[Booking]:
        # gibt eine Kopie der Buchungsliste zurück
        return self.__bookings.copy()

    def add_booking(self, booking: Booking):
        # fügt dem Zimmer eine Buchung hinzu, falls noch nicht vorhanden
        from model import Booking
        if not booking:
            raise ValueError("booking is required")
        if not isinstance(booking, Booking):
            raise ValueError("booking must be an instance of Booking")
        if booking not in self.__bookings:
            self.__bookings.append(booking)
            booking.room = self  # Rückverknüpfung setzen
