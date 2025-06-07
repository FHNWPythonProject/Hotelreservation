import pandas as pd
import model
from data_access.base_dal import BaseDal

class FacilitiesDAL(BaseDal):
    def create_facilities(self, facility_name: str) -> int:
        sql = "INSERT INTO Facilities (facility_name) VALUES (?)"
        return self.execute(sql, (facility_name,))
