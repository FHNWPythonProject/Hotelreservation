import pandas as pd
import model
from data_access.base_dal import BaseDal

class RoomTypeDAL(BaseDal):
    def create_room_type(self, description: str, max_guests: int) -> int:
        sql = "INSERT INTO Room_Type (description, max_guests) VALUES (?, ?)"
        return self.execute(sql, (description, max_guests))
