import pandas as pd
from data_access.base_dal import BaseDal
import model

class AddressDAL(BaseDal):
    def __init__(self, db_path: str = None):
        # Initialisiert Verbindung zur Datenbank
        super().__init__(db_path)

    def create_new_address(self, street: str, city: str, zip_code: str) -> model.Address:
        # Neue Adresse in die Datenbank einfügen
        if not all([street, city, zip_code]):
            raise ValueError("All address fields are required")

        sql = "INSERT INTO Address (Street, City, Zip) VALUES (?, ?, ?)"
        params = (street, city, zip_code)
        last_row_id, _ = self.execute(sql, params)
        return model.Address(address_id=last_row_id, street=street, city=city, zip_code=zip_code)

    def read_address_by_id(self, address_id: int) -> model.Address | None:
        # Eine Adresse anhand ihrer ID laden
        sql = "SELECT AddressId, Street, City, Zip FROM Address WHERE AddressId = ?"
        result = self.fetchone(sql, (address_id,))
        if result:
            id_, street, city, zip_code = result
            return model.Address(address_id=id_, street=street, city=city, zip_code=zip_code)
        return None

    def read_all_addresses(self) -> list[model.Address]:
        # Gibt alle Adressen als Liste von Objekten zurück
        sql = "SELECT AddressId, Street, City, Zip FROM Address"
        rows = self.fetchall(sql)
        return [model.Address(address_id=id_, street=street, city=city, zip_code=zip_code) for id_, street, city, zip_code in rows]

    def read_all_addresses_as_df(self) -> pd.DataFrame:
        # Gibt alle Adressen als Pandas DataFrame zurück
        sql = "SELECT AddressId, Street, City, Zip FROM Address"
        return pd.read_sql(sql, self.get_connection(), index_col="AddressId")

    def update_address(self, address: model.Address) -> None:
        # Aktualisiert eine Adresse
        sql = "UPDATE Address SET Street = ?, City = ?, Zip = ? WHERE AddressId = ?"
        params = (address.street, address.city, address.zip, address.address_id)
        self.execute(sql, params)

    def delete_address(self, address: model.Address) -> None:
        # Löscht eine Adresse anhand ihrer ID
        sql = "DELETE FROM Address WHERE AddressId = ?"
        self.execute(sql, (address.address_id,))
