from data_access.base_dal import BaseDal
from model.guest import Guest
import model
import pandas as pd

class GuestDAL(BaseDal):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)


    def read_guest_by_email(self, email: str) -> Guest | None:
        sql = """
        SELECT guest_id, first_name, last_name, email
        FROM Guest
        WHERE email = ?
        """
        row = self.fetchone(sql, (email,))
        if row:
            return Guest(guest_id=row[0], first_name=row[1], last_name=row[2], email=row[3])
        return None

    def create_guest(self, first_name: str, last_name: str, email: str) -> Guest:
        sql = """
        INSERT INTO Guest (first_name, last_name, email)
        VALUES (?, ?, ?)
        """
        guest_id, _ = self.execute(sql, (first_name, last_name, email))
        return Guest(guest_id=guest_id, first_name=first_name, last_name=last_name, email=email)

