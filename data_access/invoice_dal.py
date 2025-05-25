
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

    def read_invoice_by_id(self, invoice_id: int) -> Invoice | None:
        sql = """
        SELECT InvoiceId, Booking_Id, Total_Amount
        FROM Invoice
        WHERE Invoice_Id = ?
        """
        result = self.fetchone(sql, (invoice_id,))
        if result:
            return Invoice(
                invoice_id=result[0],
                booking_id=result[1],
                total_amount=result[2],
            )
        return None
