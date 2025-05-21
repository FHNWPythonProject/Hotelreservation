from datetime import date
from data_access.invoice_dal import InvoiceDAL
from model.invoice import Invoice


class InvoiceManager:
    def __init__(self):
        self.__invoice_dal = data_access.InvoiceDAL()

    def generate_invoice_for_booking(self, total_amount: float) -> Invoice:
        # Erstellt eine neue Rechnung mit dem übergebenen Gesamtbetrag und dem heutigen Ausstellungsdatum. Gibt das erstellte Invoice-Objekt zurück.
        return self.__invoice_dal.create_new_invoice(issue_date=date.today(), total_amount=total_amount)
