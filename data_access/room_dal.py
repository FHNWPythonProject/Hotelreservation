from datetime import date
from data_access.base_dal import BaseDal
from model.room import Room
from model.room_type import RoomType


class RoomDAL(BaseDal):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def read_all_rooms(self) -> list[Room]:
        sql = """
        SELECT Room.room_id, Room.room_number, Room.price_per_night, RoomType.max_guests, Room.hotel_id,
               RoomType.type_id, RoomType.description
        FROM Room
        JOIN Room_Type ON Room.type_id = RoomType.type_id
        """
        rows = self.fetchall(sql)
        return [
            Room(
                room_id=row[0],
                room_number=row[1],
                price_per_night=row[2],
                max_guests=row[3],
                hotel_id=row[4],
                room_type=RoomType(type_id=row[5], description=row[6])
            )
            for row in rows
        ]

    def read_rooms_by_city_and_guest_count(self, city: str, guest_count: int) -> list[Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, r.hotel_id,
               rt.type_id, rt.max_guests, rt.description
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        JOIN Address a ON h.address_id = a.address_id
        WHERE a.city = ? AND rt.max_guests >= ?
        """
        rows = self.fetchall(sql, (city, guest_count))
        return [
            Room(
                room_id=row[0],
                room_number=row[1],
                price_per_night=row[2],
                hotel_id=row[3],
                max_guests=row[5],
                room_type=RoomType(type_id=row[4], description=row[6])
            ) for row in rows
        ]

    def read_rooms_by_city_guest_count_stars_and_availability(self, city, guest_count, min_stars, checkin, checkout):
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, rt.max_guests, r.hotel_id,
               rt.type_id, rt.description
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        JOIN Address a ON h.address_id = a.address_id
        WHERE a.city = ?
          AND rt.max_guests >= ?
          AND h.stars >= ?
          AND r.room_id NOT IN (
              SELECT room_id FROM Booking
              WHERE NOT (checkout <= ? OR checkin >= ?)
          )
        """
        params = (city, guest_count, min_stars, checkin, checkout)
        rows = self.fetchall(sql, params)
        return [
            Room(
                room_id=row[0],
                room_number=row[1],
                price_per_night=row[2],
                max_guests=row[3],
                hotel_id=row[4],
                room_type=RoomType(type_id=row[5], description=row[6])
            )
            for row in rows
        ]

    def read_available_rooms(self, checkin: date, checkout: date) -> list[Room]:
        sql = """
        SELECT Room.room_id, Room.room_number, Room.price_per_night, RoomType.max_guests, Room.hotel_id,
               RoomType.type_id, RoomType.description
        FROM Room
        JOIN Room_Type ON Room.type_id = RoomType.type_id
        WHERE Room.room_id NOT IN (
            SELECT room_id FROM Booking
            WHERE NOT (checkout <= ? OR checkin >= ?)
        )
        """
        rows = self.fetchall(sql, (checkin, checkout))
        return [
            Room(
                room_id=row[0],
                room_number=row[1],
                price_per_night=row[2],
                max_guests=row[3],
                hotel_id=row[4],
                room_type=RoomType(type_id=row[5], description=row[6])
            )
            for row in rows
        ]

    def read_available_rooms_by_city_and_dates(self, city: str, checkin, checkout) -> list[Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, r.hotel_id,
               rt.type_id, rt.max_guests, rt.description
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        JOIN Address a ON h.address_id = a.address_id
        WHERE a.city = ?
        AND r.room_id NOT IN (
            SELECT room_id FROM Booking
            WHERE NOT (check_out_date <= ? OR check_in_date >= ?)
        )
        """
        rows = self.fetchall(sql, (city, checkin, checkout))
        return [
            Room(
                room_id=row[0],
                room_number=row[1],
                price_per_night=row[2],
                hotel_id=row[3],
                max_guests=row[5],
                room_type=RoomType(type_id=row[4], max_guests=row[5], description=row[6])
            ) for row in rows
        ]

    def read_available_rooms_by_city_guest_count_and_stars(self, city: str, guest_count: int, min_stars: int) -> list[Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, r.hotel_id,
               rt.type_id, rt.max_guests, rt.description
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        JOIN Address a ON h.address_id = a.address_id
        WHERE a.city = ?
          AND rt.max_guests >= ?
          AND h.stars >= ?
        """
        rows = self.fetchall(sql, (city, guest_count, min_stars))
        return [
            Room(
                room_id=row[0],
                room_number=row[1],
                price_per_night=row[2],
                hotel_id=row[3],
                max_guests=row[5],
                room_type=RoomType(type_id=row[4], max_guests=row[5], description=row[6])
            ) for row in rows
        ]

    def read_room_details(self) -> list[Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, r.hotel_id,
               rt.type_id, rt.description, rt.max_guests
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        """
        rows = self.fetchall(sql)
        return [
            Room(
                room_id=row[0],
                room_number=row[1],
                price_per_night=row[2],
                hotel_id=row[3],
                max_guests=row[6],
                room_type=RoomType(type_id=row[4], description=row[5], max_guests=row[6])
            ) for row in rows
        ]
    
    def read_available_room_details_by_date(self, checkin, checkout) -> list[Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, r.hotel_id,
               rt.type_id, rt.description, rt.max_guests
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE r.room_id NOT IN (
            SELECT room_id FROM Booking
            WHERE NOT (check_out_date <= ? OR check_in_date >= ?)
        )
        """
        rows = self.fetchall(sql, (checkin, checkout))
        return [
            Room(
                room_id=row[0],
                room_number=row[1],
                price_per_night=row[2],
                hotel_id=row[3],
                max_guests=row[6],
                room_type=RoomType(type_id=row[4], description=row[5], max_guests=row[6])
            ) for row in rows
        ]
    
    def read_room_by_id(self, room_id: int) -> Room | None:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, r.hotel_id,
               rt.type_id, rt.max_guests, rt.description
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE r.room_id = ?
        """
        result = self.fetchone(sql, (room_id,))
        if result:
            return Room(
                room_id=result[0],
                room_number=result[1],
                price_per_night=result[2],
                hotel_id=result[3],
                max_guests=result[5],
                room_type=RoomType(
                    type_id=result[4],
                    max_guests=result[5],
                    description=result[6]
                )
            )
        return None

    def read_rooms_with_facilities(self):
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night,
        rt.description AS room_type,
        GROUP_CONCAT(rf.facility_id) AS facility_ids
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        LEFT JOIN Room_Facilities rf ON r.room_id = rf.room_id
        GROUP BY r.room_id
        """
        return self.fetchall(sql)

    def update_price(self, room_id: int, new_price: float):
        sql = "UPDATE Room SET price_per_night = ? WHERE room_id = ?"
        self.execute(sql, (new_price, room_id))


