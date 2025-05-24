import sqlite3
from model.hotel import Hotel
from model.address import Address
from data_access.base_dal import BaseDal
from data_access.address_dal import AddressDAL

class HotelDAL(BaseDal):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.address_dal = AddressDAL(db_path)

    def read_all_hotels(self) -> list[Hotel]:
        sql = "SELECT hotel_id, name, stars, address_id FROM Hotel"
        rows = self.fetchall(sql)
        return [
            Hotel(
                hotel_id=row[0],
                name=row[1],
                stars=row[2],
                address=self.address_dal.read_address_by_id(row[3])
            ) for row in rows
        ]

    def read_hotels_by_city(self, city: str) -> list[Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, h.address_id
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        WHERE a.city = ?
        """
        rows = self.fetchall(sql, (city,))
        return [
            Hotel(
                hotel_id=row[0],
                name=row[1],
                stars=row[2],
                address=self.address_dal.read_address_by_id(row[3])
            ) for row in rows
        ]

    def read_hotels_by_city_and_min_stars(self, city: str, min_stars: int) -> list[Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, h.address_id
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        WHERE a.city = ? AND h.stars >= ?
        """
        rows = self.fetchall(sql, (city, min_stars))
        return [
            Hotel(
                hotel_id=row[0],
                name=row[1],
                stars=row[2],
                address=self.address_dal.read_address_by_id(row[3])
            ) for row in rows
        ]
    
    def read_hotel_by_id(self, hotel_id: int) -> Hotel | None:
        sql = "SELECT hotel_id, name, stars, address_id FROM Hotel WHERE hotel_id = ?"
        result = self.fetchone(sql, (hotel_id,))
        if result:
            return Hotel(
                hotel_id=result[0],
                name=result[1],
                stars=result[2],
                address=self.address_dal.read_address_by_id(result[3])
            )
        return None

    def read_all_hotels_with_info(self):
        sql = """
        SELECT h.hotel_id, h.name, h.stars,
               a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        """
        return self.fetchall(sql)
    
    def create_hotel(self, name: str, stars: int, address) -> Hotel:
        sql = """
        INSERT INTO Hotel (Name, Stars, Address_id)
        VALUES (?, ?, ?)
        """
        params = (name, stars, address.address_id)
        hotel_id, _ = self.execute(sql, params)
        return Hotel(hotel_id=hotel_id, name=name, stars=stars, address=address)


    def update_hotel(self, hotel: Hotel):
        sql = "UPDATE Hotel SET Name = ?, Stars = ? WHERE Hotel_Id = ?"
        params = (hotel.name, hotel.stars, hotel.hotel_id)
        self.execute(sql, params)

    def delete_hotel(self, hotel_id: int) -> None:
        sql = "DELETE FROM Hotel WHERE hotel_id = ?"
        self.execute(sql, (hotel_id,))

