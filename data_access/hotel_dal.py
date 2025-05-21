import pandas as pd
from data_access.base_dal import BaseDal
from model.hotel import Hotel
from model.address import Address

class HotelDAL(BaseDal):
    def __init__(self, db_path: str = None):
        # Initialisiert die Datenbankverbindung
        super().__init__(db_path)

    def create_new_hotel(self, name: str, stars: int) -> Hotel:
        if not name:
            raise ValueError("Hotel name is required")
        if stars is None or not isinstance(stars, int):
            raise ValueError("Stars must be an integer")

        sql = "INSERT INTO Hotel (name, stars) VALUES (?, ?)"
        params = (name, stars)
        last_row_id, _ = self.execute(sql, params)
        return Hotel(hotel_id=last_row_id, name=name, stars=stars)

    def read_hotel_by_id(self, hotel_id: int) -> Hotel | None:
        sql = "SELECT hotel_id, name, stars FROM Hotel WHERE hotel_id = ?"
        result = self.fetchone(sql, (hotel_id,))
        if result:
            hotel_id, name, stars = result
            return Hotel(hotel_id=hotel_id, name=name, stars=stars)
        return None

    def read_all_hotels(self) -> list[Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars,
           a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        """
        rows = self.fetchall(sql)

        hotels = []
        for hotel_id, name, stars, address_id, street, city, zip_code in rows:
            address = Address(address_id=address_id, street=street, city=city, zip_code=zip_code)
            hotel = Hotel(hotel_id=hotel_id, name=name, stars=stars, address=address)
            hotels.append(hotel)

        return hotels


    def read_all_hotels_as_df(self) -> pd.DataFrame:
        sql = "SELECT hotel_id, name, stars FROM Hotel"
        return pd.read_sql(sql, self.get_connection(), index_col="hotel_id")

    def update_hotel(self, hotel: Hotel) -> None:
        sql = "UPDATE Hotel SET name = ?, stars = ? WHERE hotel_id = ?"
        params = (hotel.name, hotel.stars, hotel.hotel_id)
        self.execute(sql, params)

    def delete_hotel(self, hotel: Hotel) -> None:
        sql = "DELETE FROM Hotel WHERE hotel_id = ?"
        self.execute(sql, (hotel.hotel_id,))

    def read_hotels_by_city_and_min_stars(self, city: str, min_stars: int) -> list[Hotel]:
        """
        Gibt alle Hotels in einer bestimmten Stadt mit mindestens X Sternen zurück
        """
        sql = """
        SELECT Hotel.hotel_id, Hotel.name, Hotel.stars,
               Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Address.city = ? AND Hotel.stars >= ?
        """
        params = (city, min_stars)

        rows = self.fetchall(sql, params)

        hotels = []
        for hotel_id, name, stars, address_id, street, city, zip_code in rows:
            address = Address(address_id, street, city, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)

        return hotels
    
    def read_hotels_by_city(self, city: str) -> list[Hotel]:
        """
        Gibt alle Hotels in einer bestimmten Stadt zurück
        (ohne Einschränkung auf Sterne)
        """
        sql = """
        SELECT Hotel.hotel_id, Hotel.name, Hotel.stars,
           Address.address_id, Address.street, Address.city, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE Address.city = ?
        """
        params = (city,)

        rows = self.fetchall(sql, params)

        hotels = []
        for hotel_id, name, stars, address_id, street, city, zip_code in rows:
            address = Address(address_id, street, city, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)

        return hotels
