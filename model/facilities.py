class Facilities:
    # Konstruktor: Erstellt ein neues Ausstattungsobjekt
    def __init__(self, facility_id: int, facility_name: str):
        # facility_id muss eine ganze Zahl sein
        if not isinstance(facility_id, int):
            raise ValueError("facility_id must be an integer")

        # name darf nicht leer sein
        if not facility_name:
            raise ValueError("name is required")

        # Private Attribute setzen
        self.__facility_id: int = facility_id    # eindeutige ID (z. B. 1 für WLAN)
        self.__facility_name: str = facility_name                  # Bezeichnung der Ausstattung (z. B. "TV")

    def __repr__(self):
        # Repräsentation z. B. Facilities(id=1, name='WLAN')
        return f"Facilities(id={self.__facility_id}, facility_name='{self.__facility_name}')"

    @property
    def facility_id(self) -> int:
        # Gibt die ID der Ausstattung zurück (z. B. 3 = Safe)
        return self.__facility_id

    @property
    def facility_name(self) -> str:
        # Gibt den Namen der Ausstattung zurück
        return self.__facility_name

    @facility_name.setter
    def facility_name(self, facility_name: str):
        # Erlaubt das Umbenennen der Ausstattung (z. B. "WIFI" statt "WLAN")
        if not facility_name:
            raise ValueError("facility_name cannot be empty")
        self.__facility_name = facility_name
