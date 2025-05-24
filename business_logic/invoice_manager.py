from data_access.invoice_dal import InvoiceDAL

class InvoiceManager:
    def __init__(self):
        self.invoice_dal = InvoiceDAL()

    def get_invoices_for_guest(self, guest_id: int):
        return self.invoice_dal.read_invoice_by_guest(guest_id)
