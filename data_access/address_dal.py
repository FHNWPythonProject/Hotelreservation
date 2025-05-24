import sqlite3
from data_access.base_dal import BaseDal
import model  # Stelle sicher, dass `model.address` die Address-Klasse enthält

class AddressDAL(BaseDal):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_address(self, street: str, city: str, zip_code: str) -> model.Address:
        if not all([street, city, zip_code]):
            raise ValueError("All address fields are required")

        sql = "INSERT INTO address (street, city, zip_code) VALUES (?, ?, ?)"
        params = (street, city, zip_code)
        last_row_id, _ = self.execute(sql, params)
        return model.Address(address_id=last_row_id, street=street, city=city, zip_code=zip_code)

    def read_address_by_id(self, address_id: int) -> model.Address | None:
        sql = "SELECT address_id, street, city, zip_code FROM address WHERE address_id = ?"
        result = self.fetchone(sql, (address_id,))
        if result:
            id_, street, city, zip_code = result
            return model.Address(address_id=id_, street=street, city=city, zip_code=zip_code)
        return None

    def read_all_addresses(self) -> list[model.Address]:
        sql = "SELECT address_id, street, city, zip_code FROM address"
        rows = self.fetchall(sql)
        return [
            model.Address(address_id=id_, street=street, city=city, zip_code=zip_code)
            for id_, street, city, zip_code in rows
        ]

    def update_address(self, address: model.Address) -> None:
        sql = "UPDATE address SET street = ?, city = ?, zip_code = ? WHERE address_id = ?"
        params = (address.street, address.city, address.zip_code, address.address_id)
        self.execute(sql, params)

    def delete_address(self, address: model.Address) -> None:
        sql = "DELETE FROM address WHERE address_id = ?"
        self.execute(sql, (address.address_id,))
