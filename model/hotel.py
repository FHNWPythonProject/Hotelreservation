from __future__ import annotations  # erlaubt Typverweise auf Klassen, die erst später definiert werden
from typing import TYPE_CHECKING

# dieser Block verhindert Importprobleme bei gegenseitigen Referenzen (z. B. Hotel ↔ Room)
if TYPE_CHECKING:
    from model.address import Address
    from model.room import Room


class Hotel:
    # Konstruktor: erstellt ein neues Hotel-Objekt
    def __init__(self, hotel_id: int, name: str, stars: int, address: Address = None):
        # prüft, ob hotel_id ein Integer ist
        if not isinstance(hotel_id, int):
            raise ValueError("hotel_id must be an integer")

        # prüft, ob ein Name angegeben wurde
        if not name:
            raise ValueError("name is required")

        # prüft, ob der Name ein String ist
        if not isinstance(name, str):
            raise ValueError("name must be a string")

        # prüft, ob Sterne eine gültige Zahl zwischen 1 und 5 sind
        if not isinstance(stars, int) or stars < 1 or stars > 5:
            raise ValueError("stars must be an integer between 1 and 5")

        # legt die privaten Attribute an
        self.__hotel_id: int = hotel_id
        self.__name: str = name
        self.__stars: int = stars
        self.__address: Address = address  # Adresse kann auch None sein
        self.__rooms: list[Room] = []      # leere Liste für die Zimmer des Hotels

    def __repr__(self):
        # gibt eine gut lesbare Darstellung für print() oder Debugging zurück
        return f"Hotel(id={self.__hotel_id!r}, name={self.__name!r}, stars={self.__stars!r})"

    @property
    def hotel_id(self) -> int:
        # gibt die Hotel-ID zurück (nur lesbar)
        return self.__hotel_id

    @property
    def name(self) -> str:
        # gibt den Hotelnamen zurück
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        # erlaubt es, den Hotelnamen zu ändern (mit Prüfung)
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        self.__name = name

    @property
    def stars(self) -> int:
        # gibt die Sternebewertung zurück
        return self.__stars

    @stars.setter
    def stars(self, stars: int) -> None:
        # erlaubt Änderung der Sternebewertung (nur 1–5 gültig)
        if not isinstance(stars, int) or stars < 1 or stars > 5:
            raise ValueError("stars must be an integer between 1 and 5")
        self.__stars = stars

    @property
    def address(self) -> Address:
        # gibt die Adresse zurück
        return self.__address

    @address.setter
    def address(self, address: Address) -> None:
        # erlaubt es, eine neue Adresse zu setzen (muss Address-Objekt sein)
        from model import Address  # lokal importiert, um zirkuläre Abhängigkeit zu vermeiden
        if address is not None and not isinstance(address, Address):
            raise ValueError("address must be an instance of Address")
        self.__address = address

    @property
    def rooms(self) -> list[Room]:
        # gibt eine Kopie der Zimmerliste zurück (Sicherheit durch Kapselung)
        return self.__rooms.copy()

    def add_room(self, room: Room) -> None:
        # fügt ein Zimmer zum Hotel hinzu – und verknüpft es rückwärts mit dem Hotel
        from model import Room
        if not room:
            raise ValueError("room is required")
        if not isinstance(room, Room):
            raise ValueError("room must be an instance of Room")
        if room not in self.__rooms:
            self.__rooms.append(room)
            room.hotel = self  # setzt auch im Room-Objekt das Hotel
