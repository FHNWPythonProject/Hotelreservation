
from data_access.base_dal import BaseDal
from model.invoice import Invoice

class InvoiceDAL(BaseDal):
    def create_invoice(self, booking_id: int, amount: float) -> int:
        sql = """
        INSERT INTO Invoice (Booking_Id, Total_Amount)
        VALUES (?, ?)
        """
        params = (booking_id, amount)
        last_id, _ = self.execute(sql, params)
        return last_id

    def read_invoice_by_booking_id(self, booking_id: int) -> Invoice | None:
        sql = """
        SELECT invoice_id, booking_id, total_amount
        FROM Invoice
        WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        if row:
            return Invoice(invoice_id=row[0], booking_id=row[1], total_amount=row[2])
        return None

  
    def delete_invoice(self, invoice_id: int):
        sql = "DELETE FROM Invoice WHERE invoice_id = ?"
        self.execute(sql, (invoice_id,))



