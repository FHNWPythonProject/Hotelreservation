from data_access.room_dal import RoomDAL
from model.room import Room
from datetime import date


class RoomManager:
    def __init__(self):
        self.room_dal = RoomDAL()

    def get_rooms_by_city_and_guest_count(self, city: str, guest_count: int):
        return self.room_dal.read_rooms_by_city_and_guest_count(city, guest_count)

    def get_available_rooms_by_city_and_dates(self, city: str, checkin, checkout):
        return self.room_dal.read_available_rooms_by_city_and_dates(city, checkin, checkout)

    def get_filtered_rooms(self, city: str, guest_count: int, min_stars: int):
        return self.room_dal.read_available_rooms_by_city_guest_count_and_stars(city, guest_count, min_stars)

    def get_room_details(self):
        return self.room_dal.read_room_details()

    def get_available_room_details_by_date(self, checkin, checkout):
        return self.room_dal.read_available_room_details_by_date(checkin, checkout)


