from data_access.base_dal import BaseDal
import model
import pandas as pd

class GuestDAL(BaseDal):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_guest(self, first_name: str, last_name: str, email: str) -> model.Guest:
        # Neuen Gast erstellen
        if not all([first_name, last_name, email]):
            raise ValueError("All guest fields are required")

        sql = "INSERT INTO Guest (FirstName, LastName, Email) VALUES (?, ?, ?)"
        params = (first_name, last_name, email)
        last_row_id, _ = self.execute(sql, params)
        return model.Guest(guest_id=last_row_id, first_name=first_name, last_name=last_name, email=email)

    def read_guest_by_id(self, guest_id: int) -> model.Guest | None:
        # Gast per ID lesen
        sql = "SELECT GuestId, FirstName, LastName, Email FROM Guest WHERE GuestId = ?"
        result = self.fetchone(sql, (guest_id,))
        if result:
            guest_id, first_name, last_name, email = result
            return model.Guest(guest_id, first_name, last_name, email)
        return None

    def read_all_guests(self) -> list[model.Guest]:
        # Alle Gäste als Liste
        sql = "SELECT GuestId, FirstName, LastName, Email FROM Guest"
        rows = self.fetchall(sql)
        return [model.Guest(id_, fn, ln, email) for id_, fn, ln, email in rows]

    def read_all_guests_as_df(self) -> pd.DataFrame:
        # Alle Gäste als DataFrame
        sql = "SELECT GuestId, FirstName, LastName, Email FROM Guest"
        return pd.read_sql(sql, self.get_connection(), index_col="GuestId")

    def update_guest(self, guest: model.Guest) -> None:
        # Gastdaten aktualisieren
        sql = "UPDATE Guest SET FirstName = ?, LastName = ?, Email = ? WHERE GuestId = ?"
        params = (guest.first_name, guest.last_name, guest.email, guest.guest_id)
        self.execute(sql, params)

    def delete_guest(self, guest: model.Guest) -> None:
        # Gast löschen
        sql = "DELETE FROM Guest WHERE GuestId = ?"
        self.execute(sql, (guest.guest_id,))
