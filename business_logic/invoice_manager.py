from data_access.invoice_dal import InvoiceDAL
from data_access.booking_dal import BookingDAL
from data_access.room_dal import RoomDAL
from model.invoice import Invoice

class InvoiceManager:
    def __init__(self):
        self.invoice_dal = InvoiceDAL()
        self.booking_dal = BookingDAL()
        self.room_dal = RoomDAL()

    def read_invoice_by_booking_id(self, booking_id: int) -> Invoice | None:
        return self.invoice_dal.read_invoice_by_booking_id(booking_id)

    def delete_invoice(self, invoice: Invoice):
        self.invoice_dal.delete_invoice(invoice.invoice_id)


    def generate_invoice(self, booking_id: int) -> tuple[int, float]:
        booking = self.booking_dal.read_booking_by_id(booking_id)
        if not booking:
            raise ValueError(" Buchung nicht gefunden")

        room = self.room_dal.read_room_by_id(booking.room_id)
        days = (booking.checkout_date - booking.checkin_date).days
        amount = room.price_per_night * days

        invoice_id = self.invoice_dal.create_invoice(
            booking_id=booking_id,
            amount=amount
        )
        return invoice_id, amount
