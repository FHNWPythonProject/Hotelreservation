from __future__ import annotations
from typing import TYPE_CHECKING

# Verhindert Importfehler durch zirkuläre Referenzen
if TYPE_CHECKING:
    from model.room import Room
    from model.facilities import Facilities


class RoomFacilities:
    # Konstruktor: Verknüpft ein Zimmer mit einer Ausstattung
    def __init__(self, room: Room, facility: Facilities):
        from model import Room, Facilities

        # Prüfung: room darf nicht None sein und muss vom Typ Room sein
        if not isinstance(room, Room):
            raise ValueError("room must be an instance of Room")

        # Prüfung: facility darf nicht None sein und muss vom Typ Facilities sein
        if not isinstance(facility, Facilities):
            raise ValueError("facility must be an instance of Facilities")

        # Zuweisung der Objekte (Verbindung wird hergestellt)
        self.__room: Room = room              # das Zimmer, das eine Ausstattung besitzt
        self.__facility: Facilities = facility  # die zugewiesene Ausstattung

    def __repr__(self):
        # Beispielausgabe: RoomFacilities(room=101, facility='WLAN')
        return f"RoomFacilities(room={self.__room.room_no}, facility={self.__facility.name})"

    @property
    def room(self) -> Room:
        # Gibt das Zimmerobjekt zurück
        return self.__room

    @property
    def facility(self) -> Facilities:
        # Gibt das Ausstattungsobjekt zurück
        return self.__facility
