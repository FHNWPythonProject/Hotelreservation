from data_access.room_type_dal import RoomTypeDAL

class RoomTypeManager:
    def __init__(self):
        self.room_type_dal = RoomTypeDAL()

    def create_room_type(self, description: str, max_guests: int):
        return self.room_type_dal.create_room_type(description, max_guests)