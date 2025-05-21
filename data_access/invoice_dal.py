from datetime import date
import pandas as pd
import model
from data_access.base_dal import BaseDal

class InvoiceDAL(BaseDal):
    def __init__(self, db_path: str = None):
        # Initialisiert Verbindung zur Datenbank
        super().__init__(db_path)

    def create_new_invoice(self, issue_date: date, total_amount: float) -> model.Invoice:
        # Neue Rechnung erstellen
        if issue_date is None or total_amount is None:
            raise ValueError("issue_date and total_amount are required")

        sql = "INSERT INTO Invoice (IssueDate, TotalAmount) VALUES (?, ?)"
        params = (issue_date, total_amount)
        last_row_id, _ = self.execute(sql, params)
        return model.Invoice(invoice_id=last_row_id, issue_date=issue_date, total_amount=total_amount)

    def read_invoice_by_id(self, invoice_id: int) -> model.Invoice | None:
        # Rechnung per ID lesen
        sql = "SELECT InvoiceId, IssueDate, TotalAmount FROM Invoice WHERE InvoiceId = ?"
        result = self.fetchone(sql, (invoice_id,))
        if result:
            id_, issue_date, total = result
            return model.Invoice(invoice_id=id_, issue_date=issue_date, total_amount=total)
        return None

    def read_all_invoices(self) -> list[model.Invoice]:
        # Alle Rechnungen als Liste zurückgeben
        sql = "SELECT InvoiceId, IssueDate, TotalAmount FROM Invoice"
        rows = self.fetchall(sql)
        return [model.Invoice(invoice_id=id_, issue_date=dt, total_amount=amount) for id_, dt, amount in rows]

    def read_all_invoices_as_df(self) -> pd.DataFrame:
        # Alle Rechnungen als DataFrame zurückgeben
        sql = "SELECT InvoiceId, IssueDate, TotalAmount FROM Invoice"
        return pd.read_sql(sql, self.get_connection(), index_col="InvoiceId")

    def update_invoice(self, invoice: model.Invoice) -> None:
        # Rechnung aktualisieren
        sql = "UPDATE Invoice SET IssueDate = ?, TotalAmount = ? WHERE InvoiceId = ?"
        params = (invoice.issue_date, invoice.total_amount, invoice.invoice_id)
        self.execute(sql, params)

    def delete_invoice(self, invoice: model.Invoice) -> None:
        # Rechnung löschen
        sql = "DELETE FROM Invoice WHERE InvoiceId = ?"
        self.execute(sql, (invoice.invoice_id,))
