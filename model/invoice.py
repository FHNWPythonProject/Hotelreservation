from datetime import date

class Invoice:
    # Konstruktor: erstellt ein neues Rechnungsobjekt
    def __init__(self, invoice_id: int, issue_date: date, total_amount: float):
        # ID muss ein Integer sein
        if not isinstance(invoice_id, int):
            raise ValueError("invoice_id must be an integer")

        # issue_date muss ein gültiges Datum sein
        if not isinstance(issue_date, date):
            raise ValueError("issue_date must be a date object")

        # Gesamtbetrag muss ein positiver Float oder Integer sein
        if not isinstance(total_amount, (int, float)) or total_amount <= 0:
            raise ValueError("total_amount must be a positive number")

        # Attribute setzen (alle privat, d. h. mit __)
        self.__invoice_id: int = invoice_id                # eindeutige Rechnungsnummer
        self.__issue_date: date = issue_date               # Ausstellungsdatum der Rechnung
        self.__total_amount: float = total_amount          # Betrag in € / CHF / etc.

    def __repr__(self):
        # Repräsentation zur besseren Lesbarkeit beim Debugging oder Drucken
        return f"Invoice(id={self.__invoice_id}, date={self.__issue_date}, total={self.__total_amount})"

    @property
    def invoice_id(self) -> int:
        # gibt die Rechnungs-ID zurück (read-only)
        return self.__invoice_id

    @property
    def issue_date(self) -> date:
        # gibt das Ausstellungsdatum zurück
        return self.__issue_date 

    @issue_date.setter
    def issue_date(self, value: date):
        # erlaubt Änderung des Datums (z. B. falls falsches Datum gespeichert wurde)
        if not isinstance(value, date):
            raise ValueError("issue_date must be a date")
        self.__issue_date = value

    @property
    def total_amount(self) -> float:
        # gibt den Gesamtbetrag der Rechnung zurück
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value: float):
        # erlaubt Änderung des Betrags (z. B. wenn Rabatte hinzugefügt werden)
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("total_amount must be a positive number")
        self.__total_amount = value
