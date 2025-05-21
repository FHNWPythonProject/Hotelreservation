from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.hotel import Hotel
    from model.room_type import RoomType
    from model.booking import Booking


class Room:
    # Konstruktor: erstellt ein neues Zimmer
    def __init__(self, room_no: int, price_per_night: float, hotel: Hotel = None, room_type: RoomType = None):
        # room_no muss eine ganze Zahl sein
        if not isinstance(room_no, int):
            raise ValueError("room_no must be an integer")

        # Preis muss float oder int und > 0 sein
        if not isinstance(price_per_night, (int, float)) or price_per_night <= 0:
            raise ValueError("price_per_night must be a positive number")

        self.__room_no: int = room_no
        self.__price_per_night: float = price_per_night
        self.__hotel: Hotel = hotel
        self.__room_type: RoomType = room_type
        self.__bookings: list[Booking] = []  # Liste aller Buchungen für dieses Zimmer

        # Verknüpfe dieses Zimmer mit dem Hotel (wenn angegeben)
        if hotel:
            hotel.add_room(self)

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
