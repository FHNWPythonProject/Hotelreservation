from data_access.room_dal import RoomDAL
from model.room import Room
from datetime import date


class RoomManager:
    def __init__(self):
        self.__room_dal = data_access.RoomDAL()

    def get_rooms_cheaper_than(self, max_price: float) -> list[Room]:
        # Gibt alle Zimmer zurück, deren Preis unterhalb des Limits liegt
        all_rooms = self.__room_dal.read_all_rooms()
        return [room for room in all_rooms if room.price_per_night <= max_price]

    def get_available_rooms(self, checkin: date, checkout: date) -> list[Room]:
        # Gibt alle Zimmer zurück, die im angegebenen Zeitraum verfügbar sind.
        return self._room_dal.read_available_rooms(checkin, checkout)

