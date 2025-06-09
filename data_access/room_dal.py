from datetime import date
from data_access.base_dal import BaseDal
from model.room import Room
from model.room_type import RoomType
from model.facilities import Facilities


class RoomDAL(BaseDal):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def read_all_rooms(self) -> list[Room]:
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
                room_type=RoomType(type_id=row[4], description=row[5], max_guests=row[6])
            ) for row in rows
        ]

    def read_rooms_by_city_and_guest_count(self, city: str, guest_count: int) -> list[Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, r.hotel_id,
               rt.type_id, rt.description, rt.max_guests
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
                room_type=RoomType(type_id=row[4], description=row[5], max_guests=row[6])
            ) for row in rows
        ]

    def read_available_rooms_by_city_and_dates(self, city: str, checkin: date, checkout: date) -> list[Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, r.hotel_id,
               rt.type_id, rt.description, rt.max_guests
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
                room_type=RoomType(type_id=row[4], description=row[5], max_guests=row[6])
            ) for row in rows
        ]

    def read_available_rooms_by_city_guest_count_and_stars(self, city: str, guest_count: int, min_stars: int) -> list[Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, r.hotel_id,
               rt.type_id, rt.description, rt.max_guests
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
                room_type=RoomType(type_id=row[4], description=row[5], max_guests=row[6])
            ) for row in rows
        ]

    def read_room_by_id(self, room_id: int) -> Room | None:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, r.hotel_id,
               rt.type_id, rt.description, rt.max_guests
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
                room_type=RoomType(type_id=result[4], description=result[5], max_guests=result[6])
            )
        return None

    def read_available_room_details_by_date(self, checkin: date, checkout: date) -> list[Room]:
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
                room_type=RoomType(type_id=row[4], description=row[5], max_guests=row[6])
            ) for row in rows
        ]

    def update_price(self, room_id: int, new_price: float):
        sql = "UPDATE Room SET price_per_night = ? WHERE room_id = ?"
        self.execute(sql, (new_price, room_id))

    def read_room_details_with_facilities(self) -> list[Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, r.hotel_id,
            rt.type_id, rt.description, rt.max_guests,
            f.facility_id, f.facility_name
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        LEFT JOIN Room_Facilities rf ON r.room_id = rf.room_id
        LEFT JOIN Facilities f ON rf.facility_id = f.facility_id
        ORDER BY r.room_id
        """
        rows = self.fetchall(sql)

        rooms_dict = {}
        for row in rows:
            room_id = row[0]
            if room_id not in rooms_dict:
                room = Room(
                    room_id=row[0],
                    room_number=row[1],
                    price_per_night=row[2],
                    hotel_id=row[3],
                    room_type=RoomType(type_id=row[4], description=row[5], max_guests=row[6])
                )
                room.facilities = []
                rooms_dict[room_id] = room

            # falls Ausstattung vorhanden
            if row[7]:
                rooms_dict[room_id].facilities.append(Facilities(facility_id=row[7], facility_name=row[8]))

        return list(rooms_dict.values())


    def read_available_rooms_by_type_and_date(self, room_type_description: str, checkin, checkout) -> list[Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, r.hotel_id,
            rt.type_id, rt.max_guests, rt.description
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE rt.description = ?
        AND r.room_id NOT IN (
            SELECT room_id FROM Booking
            WHERE NOT (check_out_date <= ? OR check_in_date >= ?)
        )
        """
        rows = self.fetchall(sql, (room_type_description, checkin, checkout))
        return [
            Room(
                room_id=row[0],
                room_number=row[1],
                price_per_night=row[2],
                hotel_id=row[3],
                room_type=RoomType(type_id=row[4], max_guests=row[5], description=row[6])
            )
            for row in rows
        ]
