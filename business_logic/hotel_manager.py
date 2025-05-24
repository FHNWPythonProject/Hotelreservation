from data_access.hotel_dal import HotelDAL

class HotelManager:
    def __init__(self):
        self.hotel_dal = HotelDAL()

    def get_hotels_by_city(self, city: str):
        return self.hotel_dal.read_hotels_by_city(city)

    def get_hotels_by_city_and_stars(self, city: str, min_stars: int):
        return self.hotel_dal.read_hotels_by_city_and_min_stars(city, min_stars)

    def get_hotel_by_id(self, hotel_id: int):
        return self.hotel_dal.read_hotel_by_id(hotel_id)
    
    def get_all_hotels_with_info(self):
        return self.hotel_dal.read_all_hotels_with_info()





        