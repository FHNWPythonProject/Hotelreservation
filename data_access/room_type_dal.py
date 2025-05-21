import pandas as pd
import model
from data_access.base_dal import BaseDal

class RoomTypeDAL(BaseDal):
    def __init__(self, db_path: str = None):
        # Initialisiert Datenbankzugriff
        super().__init__(db_path)

    def create_new_room_type(self, description: str, max_guests: int) -> model.RoomType:
        # Neuen Zimmertyp anlegen
        if not description:
            raise ValueError("Description is required")
        if max_guests is None or not isinstance(max_guests, int):
            raise ValueError("Max guests must be an integer")

        sql = "INSERT INTO RoomType (Description, MaxGuests) VALUES (?, ?)"
        params = (description, max_guests)
        last_row_id, _ = self.execute(sql, params)
        return model.RoomType(room_type_id=last_row_id, description=description, max_guests=max_guests)

    def read_room_type_by_id(self, room_type_id: int) -> model.RoomType | None:
        # Zimmertyp nach ID auslesen
        sql = "SELECT RoomTypeId, Description, MaxGuests FROM RoomType WHERE RoomTypeId = ?"
        result = self.fetchone(sql, (room_type_id,))
        if result:
            id_, desc, max_g = result
            return model.RoomType(room_type_id=id_, description=desc, max_guests=max_g)
        return None

    def read_all_room_types(self) -> list[model.RoomType]:
        # Alle Zimmertypen als Liste zurückgeben
        sql = "SELECT RoomTypeId, Description, MaxGuests FROM RoomType"
        rows = self.fetchall(sql)
        return [model.RoomType(room_type_id=id_, description=desc, max_guests=max_g) for id_, desc, max_g in rows]

    def read_all_room_types_as_df(self) -> pd.DataFrame:
        # Alle Zimmertypen als DataFrame
        sql = "SELECT RoomTypeId, Description, MaxGuests FROM RoomType"
        return pd.read_sql(sql, self.get_connection(), index_col="RoomTypeId")

    def update_room_type(self, room_type: model.RoomType) -> None:
        # Zimmertyp aktualisieren
        sql = "UPDATE RoomType SET Description = ?, MaxGuests = ? WHERE RoomTypeId = ?"
        params = (room_type.description, room_type.max_guests, room_type.room_type_id)
        self.execute(sql, params)

    def delete_room_type(self, room_type: model.RoomType) -> None:
        # Zimmertyp löschen
        sql = "DELETE FROM RoomType WHERE RoomTypeId = ?"
        self.execute(sql, (room_type.room_type_id,))
