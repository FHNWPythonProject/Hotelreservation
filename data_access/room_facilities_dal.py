import model
from data_access.base_dal import BaseDal
import pandas as pd

class RoomFacilitiesDAL(BaseDal):
    def __init__(self, db_path: str = None):
        # Verbindung zur Datenbank aufbauen
        super().__init__(db_path)

    def add_facility_to_room(self, room_no: int, facility_id: int) -> None:
        # Fügt einem Zimmer eine Ausstattung hinzu (Join-Eintrag)
        sql = "INSERT INTO RoomFacilities (RoomNo, FacilityId) VALUES (?, ?)"
        params = (room_no, facility_id)
        self.execute(sql, params)

    def remove_facility_from_room(self, room_no: int, facility_id: int) -> None:
        # Entfernt eine Ausstattung vom Zimmer
        sql = "DELETE FROM RoomFacilities WHERE RoomNo = ? AND FacilityId = ?"
        self.execute(sql, (room_no, facility_id))

    def get_facilities_for_room(self, room_no: int) -> list[model.Facilities]:
        # Gibt alle Facilities für ein Zimmer zurück
        sql = """
        SELECT f.FacilityId, f.Name
        FROM RoomFacilities rf
        JOIN Facilities f ON rf.FacilityId = f.FacilityId
        WHERE rf.RoomNo = ?
        """
        rows = self.fetchall(sql, (room_no,))
        return [model.Facilities(facility_id=id_, name=name) for id_, name in rows]

    def get_rooms_with_facility(self, facility_id: int) -> list[int]:
        # Gibt alle Zimmernummern zurück, die diese Ausstattung haben
        sql = "SELECT RoomNo FROM RoomFacilities WHERE FacilityId = ?"
        rows = self.fetchall(sql, (facility_id,))
        return [room_no for (room_no,) in rows]

    def get_all_as_df(self) -> pd.DataFrame:
        # Gibt die gesamte RoomFacilities-Tabelle als DataFrame zurück
        sql = "SELECT RoomNo, FacilityId FROM RoomFacilities"
        return pd.read_sql(sql, self.get_connection())

    def get_facilities_for_room(self, room_id: int) -> list[model.Facilities]:
        sql = """
        SELECT f.FacilityId, f.FacilityName
        FROM Facilities f
        JOIN Room_Facilities rf ON f.FacilityId = rf.FacilityId
        WHERE rf.RoomId = ?
        """
        rows = self.fetchall(sql, (room_id,))
        return [model.Facilities(facility_id=id_, facility_name=name) for id_, name in rows]
