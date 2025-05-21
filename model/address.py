class Address:
    def __init__(self, address_id: int, street: str, city: str, zipcode: str):
        # Der Konstruktor initialisiert die Adresse mit allen Feldern
        # Die Werte werden auf Gültigkeit geprüft
        if not isinstance(address_id, int):
            raise ValueError("address_id must be an integer")
        if not street:
            raise ValueError("street is required")
        if not city:
            raise ValueError("city is required")
        if not zip_code:
            raise ValueError("zip is required")

        # Private Attribute zur Kapselung der Daten
        self.__address_id = address_id
        self.__street = street
        self.__city = city
        self.__zip = zip_code

    def __repr__(self):
        # Gibt eine lesbare Darstellung der Adresse zurück (z.B. für print())
        return f"Address(id={self.__address_id}, street={self.__street}, city={self.__city}, zip={self.__zip})"

    # ===================================================
    # Getter für address_id (nur lesbar, keine Änderung erlaubt)
    @property
    def address_id(self) -> int:
        return self.__address_id

    # ===================================================
    # Getter und Setter für street
    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        # Setter prüft, ob der neue Straßenname gültig ist
        if not street:
            raise ValueError("street cannot be empty")
        self.__street = street

    # ===================================================
    # Getter und Setter für city
    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        # Setter prüft, ob der neue Stadtname gültig ist
        if not city:
            raise ValueError("city cannot be empty")
        self.__city = city

    # ===================================================
    # Getter und Setter für zip (Postleitzahl)
    @property
    def zip(self) -> str:
        return self.__zip

    @zip.setter
    def zip(self, zip_code: str):
        # Setter prüft, ob die neue PLZ gültig ist
        if not zip_code:
            raise ValueError("zip cannot be empty")
        self.__zip = zip_code
