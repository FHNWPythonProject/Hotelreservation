from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.hotel import Hotel
    from model.room_type import RoomType
    from model.booking import Booking


class Room:
    def __init__(
        self,
        room_id: int,
        room_number: str,
        price_per_night: float,
        hotel_id: int,
        room_type: RoomType = None
    ):
        self.room_id = room_id
        self._room_number = room_number
        self._price_per_night = price_per_night
        self.hotel_id = hotel_id
        self._room_type = room_type
        self._bookings: list[Booking] = []
        self.facilities = []

    def __repr__(self):
        return f"Room(no={self._room_number}, price={self._price_per_night})"

    @property
    def room_number(self) -> str:
        return self._room_number

    @property
    def price_per_night(self) -> float:
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, price: float):
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("price must be a positive number")
        self._price_per_night = price

    @property
    def room_type(self) -> RoomType:
        return self._room_type

    @room_type.setter
    def room_type(self, room_type: RoomType):
        from model.room_type import RoomType
        if room_type is not None and not isinstance(room_type, RoomType):
            raise ValueError("room_type must be an instance of RoomType")
        self._room_type = room_type

    @property
    def bookings(self) -> list[Booking]:
        return self._bookings.copy()

    def add_booking(self, booking: Booking):
        from model.booking import Booking
        if not isinstance(booking, Booking):
            raise ValueError("booking must be a Booking instance")
        if booking not in self._bookings:
            self._bookings.append(booking)
            booking.room = self  # Rückverknüpfung
