from datetime import datetime
from data_access.base_dal import BaseDal
from model.booking import Booking
import pandas as pd

class BookingDAL(BaseDal):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_booking(self, guest_id: int, room_no: int, checkin: datetime, checkout: datetime, total_amount: float) -> Booking:
        # Neue Buchung erstellen
        sql = """
        INSERT INTO Booking (GuestId, RoomNo, Checkin, Checkout, TotalAmount, IsCancelled)
        VALUES (?, ?, ?, ?, ?, 0)
        """
        params = (guest_id, room_no, checkin, checkout, total_amount)
        last_row_id, _ = self.execute(sql, params)
        return Booking(booking_id=last_row_id, guest=None, room=None,
                             checkin=checkin, checkout=checkout, total_amount=total_amount)

    def read_booking_by_id(self, booking_id: int) -> Booking | None:
        # Buchung lesen
        sql = """
        SELECT BookingId, GuestId, RoomNo, Checkin, Checkout, TotalAmount, IsCancelled
        FROM Booking WHERE BookingId = ?
        """
        result = self.fetchone(sql, (booking_id,))
        if result:
            booking_id, guest_id, room_no, checkin, checkout, total_amount, is_cancelled = result
            booking = Booking(booking_id, guest=None, room=None, checkin=checkin, checkout=checkout, total_amount=total_amount)
            if is_cancelled:
                booking.cancel()
            return booking
        return None

    def read_all_bookings(self) -> list[Booking]:
        # Alle Buchungen als Liste
        sql = "SELECT BookingId, GuestId, RoomNo, Checkin, Checkout, TotalAmount, IsCancelled FROM Booking"
        rows = self.fetchall(sql)
        bookings = []
        for b in rows:
            booking = Booking(b[0], guest=None, room=None, checkin=b[3], checkout=b[4], total_amount=b[5])
            if b[6]:
                booking.cancel()
            bookings.append(booking)
        return bookings

    def read_all_bookings_as_df(self) -> pd.DataFrame:
        # Alle Buchungen als DataFrame
        sql = "SELECT BookingId, GuestId, RoomNo, Checkin, Checkout, TotalAmount, IsCancelled FROM Booking"
        return pd.read_sql(sql, self.get_connection(), index_col="BookingId")

    def update_booking(self, booking: Booking) -> None:
        # Buchung aktualisieren
        sql = """
        UPDATE Booking SET Checkin = ?, Checkout = ?, TotalAmount = ?, IsCancelled = ?
        WHERE BookingId = ?
        """
        params = (booking.checkin, booking.checkout, booking.total_amount, booking.is_cancelled, booking.booking_id)
        self.execute(sql, params)

    def delete_booking(self, booking: Booking) -> None:
        # Buchung löschen
        sql = "DELETE FROM Booking WHERE BookingId = ?"
        self.execute(sql, (booking.booking_id,))

    def is_room_available(self, room_no: int, checkin: datetime, checkout: datetime) -> bool:
        # Prüfen, ob ein Zimmer im Zeitraum verfügbar ist
        sql = """
        SELECT COUNT(*) FROM Booking
        WHERE RoomNo = ? AND IsCancelled = 0
        AND (Checkin < ? AND Checkout > ?)
        """
        params = (room_no, checkout, checkin)
        result = self.fetchone(sql, params)
        return result[0] == 0
