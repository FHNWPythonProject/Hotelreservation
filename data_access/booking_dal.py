from data_access.base_dal import BaseDal
from model.booking import Booking
from datetime import datetime

class BookingDAL(BaseDal):
    def read_booking_by_id(self, booking_id: int) -> Booking | None:
        # Eine Buchung anhand ihrer ID laden
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, total_amount, is_cancelled
        FROM Booking
        WHERE booking_id = ?
        """
        result = self.fetchone(sql, (booking_id,))
        if result:
            return Booking(
                booking_id=result[0],
                guest_id=result[1],
                room_id=result[2],
                checkin_date=result[3],
                checkout_date=result[4],
                total_amount=result[5],
                is_cancelled=bool(result[6])
            )
        return None

    def read_all_bookings(self) -> list[Booking]:
        # Alle Buchungen laden
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, total_amount, is_cancelled
        FROM Booking
        """
        rows = self.fetchall(sql)
        return [
            Booking(
                booking_id=row[0],
                guest_id=row[1],
                room_id=row[2],
                checkin_date=row[3],
                checkout_date=row[4],
                total_amount=row[5],
                is_cancelled=bool(row[6])
            )
            for row in rows
        ]

    def create_booking(self, booking: Booking) -> int:
        # Neue Buchung einfügen
        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, total_amount, is_cancelled)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (
            booking.guest_id,
            booking.room_id,
            booking.checkin_date,
            booking.checkout_date,
            booking.total_amount,
            int(booking.is_cancelled)
        )
        booking_id, _ = self.execute(sql, params)
        return booking_id

    def delete_booking(self, booking_id: int) -> None:
        # Buchung löschen
        sql = "DELETE FROM Booking WHERE booking_id = ?"
        self.execute(sql, (booking_id,))

    def read_all_bookings_with_hotel_info(self):
        sql = """
        SELECT 
            b.booking_id, h.name, r.room_number, 
            b.check_in_date, b.check_out_date, 
            b.total_amount, b.is_cancelled
        FROM Booking b
        JOIN Room r ON b.room_id = r.room_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        ORDER BY b.check_in_date DESC
        """
        return self.fetchall(sql)

    
    def delete_booking_by_id(self, booking_id: int) -> bool:
        sql = "DELETE FROM Booking WHERE booking_id = ?"
        _, rowcount = self.execute(sql, (booking_id,))
        return rowcount > 0
        

    def update_phone_number(self, booking_id: int, phone_number: str) -> None:
        # Aktualisiert die Telefonnummer einer Buchung.
        sql = "UPDATE Booking SET PhoneNumber = ? WHERE BookingId = ?"
        self.execute(sql, (phone_number, booking_id))
