from data_access.hotel_dal import HotelDAL
from data_access.address_dal import AddressDAL
from model.hotel import Hotel

class HotelManager:
    def __init__(self):
        self.hotel_dal = HotelDAL()
        self.address_dal = AddressDAL()

    def get_hotels_by_city(self, city: str):
        return self.hotel_dal.read_hotels_by_city(city)

    def get_hotels_by_city_and_stars(self, city: str, min_stars: int):
        return self.hotel_dal.read_hotels_by_city_and_min_stars(city, min_stars)

    def get_hotel_by_id(self, hotel_id: int):
        return self.hotel_dal.read_hotel_by_id(hotel_id)
    
    def get_all_hotels_with_info(self):
        return self.hotel_dal.read_all_hotels_with_info()

    def create_hotel(self, name: str, stars: int, city: str, street: str, zip_code: str) -> Hotel:
        # Adresse erstellen
        new_address = self.address_dal.create_new_address(street=street, city=city, zip_code=zip_code)
        
        # Hotel mit der erstellten Adresse speichern
        return self.hotel_dal.create_hotel(name=name, stars=stars, address=new_address)

    def update_hotel(self, hotel: Hotel):
        self.hotel_dal.update_hotel(hotel)

    def delete_hotel(self, hotel_id: int):
        self.hotel_dal.delete_hotel(hotel_id)





        