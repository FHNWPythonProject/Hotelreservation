import pandas as pd
import model
from data_access.base_dal import BaseDal

class FacilitiesDAL(BaseDal):
    def __init__(self, db_path: str = None):
        # Datenbankverbindung initialisieren
        super().__init__(db_path)

    def create_new_facility(self, name: str) -> model.Facilities:
        # Neue Ausstattung einfügen
        if not name:
            raise ValueError("Facility name is required")

        sql = "INSERT INTO Facilities (Name) VALUES (?)"
        params = (name,)
        last_row_id, _ = self.execute(sql, params)
        return model.Facilities(facility_id=last_row_id, name=name)

    def read_facility_by_id(self, facility_id: int) -> model.Facilities | None:
        # Eine Ausstattung per ID lesen
        sql = "SELECT FacilityId, Name FROM Facilities WHERE FacilityId = ?"
        result = self.fetchone(sql, (facility_id,))
        if result:
            id_, name = result
            return model.Facilities(facility_id=id_, name=name)
        return None

    def read_all_facilities(self) -> list[model.Facilities]:
        # Liste aller Ausstattungen
        sql = "SELECT FacilityId, Name FROM Facilities"
        rows = self.fetchall(sql)
        return [model.Facilities(facility_id=id_, name=name) for id_, name in rows]

    def read_all_facilities_as_df(self) -> pd.DataFrame:
        # Als Pandas DataFrame
        sql = "SELECT FacilityId, Name FROM Facilities"
        return pd.read_sql(sql, self.get_connection(), index_col="FacilityId")

    def update_facility(self, facility: model.Facilities) -> None:
        # Ausstattung umbenennen
        sql = "UPDATE Facilities SET Name = ? WHERE FacilityId = ?"
        params = (facility.name, facility.facility_id)
        self.execute(sql, params)

    def delete_facility(self, facility: model.Facilities) -> None:
        # Ausstattung löschen
        sql = "DELETE FROM Facilities WHERE FacilityId = ?"
        self.execute(sql, (facility.facility_id,))
