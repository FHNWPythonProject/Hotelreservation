import pandas as pd
import model
import data_access

class GuestManager:
    def __init__(self):
        self.__guest_dal = data_access.GuestDAL()

    def create_guest(self, first_name: str, last_name: str, email: str) -> model.Guest:
        # Erstellt neuen Gast
        return self.__guest_dal.create_new_guest(first_name, last_name, email)

    def read_guest(self, guest_id: int) -> model.Guest | None:
        # Gast anhand ID lesen
        return self.__guest_dal.read_guest_by_id(guest_id)

    def read_all_guests(self) -> list[model.Guest]:
        # Alle Gäste als Liste
        return self.__guest_dal.read_all_guests()

    def read_all_guests_as_df(self) -> pd.DataFrame:
        # Alle Gäste als DataFrame
        return self.__guest_dal.read_all_guests_as_df()

    def update_guest(self, guest: model.Guest) -> None:
        # Gastdaten aktualisieren
        self.__guest_dal.update_guest(guest)

    def delete_guest(self, guest: model.Guest) -> None:
        # Gast löschen
        self.__guest_dal.delete_guest(guest)
