class RoomType:
    def __init__(self, type_id: int, description: str, max_guests: int):
        self._type_id = type_id
        self._description = description
        self._max_guests = max_guests

    # === Getter für type_id ===
    @property
    def type_id(self) -> int:
        return self._type_id

    # === Getter & Setter für description ===
    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        if not value:
            raise ValueError("description cannot be empty")
        self._description = value

    # === Getter & Setter für max_guests ===
    @property
    def max_guests(self) -> int:
        return self._max_guests

    @max_guests.setter
    def max_guests(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("max_guests must be a positive integer")
        self._max_guests = value

    def __repr__(self):
        return f"RoomType(type_id={self._type_id}, description='{self._description}', max_guests={self._max_guests})"
