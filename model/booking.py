from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date  # zum Arbeiten mit Check-in / Check-out

# Verhindert Importfehler bei zirkulären Abhängigkeiten
if TYPE_CHECKING:
    from model.room import Room
    from model.guest import Guest
    from model.invoice import Invoice


class Booking:
    # Konstruktor: erstellt ein neues Booking-Objekt
    def __init__(
        self,
        booking_id: int,
        checkin: date,
        checkout: date,
        total_amount: float,
        guest: Guest = None,
        room: Room = None
    ):
        # Prüfung: booking_id muss ein Integer sein
        if not isinstance(booking_id, int):
            raise ValueError("booking_id must be an integer")

        # Prüfung: checkin und checkout müssen Datumsobjekte sein
        if not isinstance(checkin, date) or not isinstance(checkout, date):
            raise ValueError("checkin and checkout must be date objects")

        # Logik: Check-out muss nach dem Check-in liegen
        if checkin >= checkout:
            raise ValueError("checkout must be after checkin")

        # Prüfung: Preis muss eine positive Zahl sein
        if not isinstance(total_amount, (int, float)) or total_amount <= 0:
            raise ValueError("total_amount must be a positive number")

        # Private Attribute setzen
        self.__booking_id: int = booking_id
        self.__checkin: date = checkin
        self.__checkout: date = checkout
        self.__total_amount: float = total_amount
        self.__guest: Guest = guest       # optional beim Erstellen
        self.__room: Room = room          # optional beim Erstellen
        self.__is_cancelled: bool = False # initial: Buchung ist nicht storniert
        self.__invoice: Invoice = None    # Rechnung wird später zugewiesen

        # Rückverknüpfung mit Guest & Room setzen (wenn übergeben)
        if guest:
            guest.add_booking(self)
        if room:
            room.add_booking(self)

    def __repr__(self):
        # Textdarstellung z. B. Booking(id=4, from=2025-06-01, to=2025-06-07)
        return f"Booking(id={self.__booking_id}, from={self.__checkin}, to={self.__checkout})"

    # -----------------------------------------
    @property
    def booking_id(self) -> int:
        # gibt die eindeutige Buchungs-ID zurück
        return self.__booking_id

    @property
    def checkin(self) -> date:
        # Rückgabe des Check-in-Datums
        return self.__checkin

    @property
    def checkout(self) -> date:
        # Rückgabe des Check-out-Datums
        return self.__checkout

    @property
    def total_amount(self) -> float:
        # Rückgabe des Rechnungsbetrags
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, amount: float):
        # erlaubt, den Rechnungsbetrag zu ändern (z. B. Rabatt)
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("total_amount must be positive")
        self.__total_amount = amount

    @property
    def is_cancelled(self) -> bool:
        # zeigt an, ob die Buchung storniert wurde
        return self.__is_cancelled

    def cancel(self):
        # Methode zum Stornieren der Buchung
        self.__is_cancelled = True

    @property
    def guest(self) -> Guest:
        # gibt den verknüpften Gast zurück
        return self.__guest

    @guest.setter
    def guest(self, guest: Guest):
        from model import Guest
        if guest is not None and not isinstance(guest, Guest):
            raise ValueError("guest must be a Guest instance")
        self.__guest = guest

    @property
    def room(self) -> Room:
        # gibt das zugeordnete Zimmer zurück
        return self.__room

    @room.setter
    def room(self, room: Room):
        from model import Room
        if room is not None and not isinstance(room, Room):
            raise ValueError("room must be a Room instance")
        self.__room = room

    @property
    def invoice(self) -> Invoice:
        # gibt die zugehörige Rechnung zurück
        return self.__invoice

    @invoice.setter
    def invoice(self, invoice: Invoice):
        from model import Invoice
        if invoice is not None and not isinstance(invoice, Invoice):
            raise ValueError("invoice must be an Invoice instance")
        self.__invoice = invoice
