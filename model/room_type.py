class RoomType:
    # Konstruktor: erstellt ein neues Zimmer-Typ-Objekt
    def __init__(self, room_type_id: int, description: str, max_guests: int):
        # room_type_id muss int sein
        if not isinstance(room_type_id, int):
            raise ValueError("room_type_id must be an integer")

        # Beschreibung darf nicht leer sein
        if not description:
            raise ValueError("description is required")

        # max_guests muss int > 0 sein
        if not isinstance(max_guests, int) or max_guests <= 0:
            raise ValueError("max_guests must be a positive integer")

        self.__room_type_id: int = room_type_id
        self.__description: str = description
        self.__max_guests: int = max_guests

    def __repr__(self):
        # Darstellung z. B. RoomType(id=1, "Suite", 2 Gäste)
        return f"RoomType(id={self.__room_type_id}, desc={self.__description}, max={self.__max_guests})"

    @property
    def room_type_id(self) -> int:
        return self.__room_type_id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, text: str):
        # setzt Beschreibung neu (muss String sein)
        if not text:
            raise ValueError("description is required")
        self.__description = text

    @property
    def max_guests(self) -> int:
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, count: int):
        # neue maximale Gästeanzahl setzen
        if not isinstance(count, int) or count <= 0:
            raise ValueError("max_guests must be a positive integer")
        self.__max_guests = count
