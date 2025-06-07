from data_access.room_dal import RoomDAL
from model.room import Room
from model.room_type import RoomType
from model.hotel import Hotel
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

    def apply_dynamic_pricing(self, base_price: float, checkin: date) -> float:
        month = checkin.month
        if month in [7, 8]:  # Juli, August
            return base_price * 1.20
        elif month in [1, 2]:  # Januar, Februar
            return base_price * 0.85
        return base_price

    def get_dynamic_room_prices(self, checkin, checkout):
        rooms = self.room_dal.read_available_room_details_by_date(checkin, checkout)
        for room in rooms:
            room.price_per_night = self.apply_dynamic_pricing(room.price_per_night, checkin)
        return rooms

    def get_rooms_with_facilities(self):
        return self.room_dal.read_rooms_with_facilities()
    
    def update_price(self, room_id: int, new_price: float):
        self.room_dal.update_price(room_id, new_price)

    def get_room_details_with_facilities(self):
        return self.room_dal.read_room_details_with_facilities()

