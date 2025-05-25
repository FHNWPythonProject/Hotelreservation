import pandas as pd
import model
from data_access.base_dal import BaseDal

class FacilitiesDAL(BaseDal):
    def create_facility(self, description: str) -> int:
        sql = "INSERT INTO Facilities (description) VALUES (?)"
        return self.execute(sql, (description,))
