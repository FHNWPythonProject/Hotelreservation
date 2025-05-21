from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.address import Address
    from model.booking import Booking


class Guest:
    # Konstruktor: erstellt ein neues Gastobjekt
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, address: Address = None):
        # prüft, ob guest_id eine gültige ganze Zahl ist
        if not isinstance(guest_id, int):
            raise ValueError("guest_id must be an integer")

        # Vorname muss angegeben sein
        if not first_name:
            raise ValueError("first_name is required")

        # Nachname muss angegeben sein
        if not last_name:
            raise ValueError("last_name is required")

        # E-Mail-Adresse muss angegeben sein
        if not email:
            raise ValueError("email is required")

        self.__guest_id: int = guest_id
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__email: str = email
        self.__address: Address = address  # Adresse ist optional
        self.__bookings: list[Booking] = []  # Liste der Buchungen dieses Gastes

    def __repr__(self):
        # einfache Textdarstellung des Gastes
        return f"Guest(id={self.__guest_id}, name='{self.__first_name} {self.__last_name}')"

    @property
    def guest_id(self) -> int:
        # gibt die ID zurück (read-only)
        return self.__guest_id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, name: str):
        # erlaubt Änderung des Vornamens
        if not name:
            raise ValueError("first_name is required")
        self.__first_name = name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, name: str):
        # erlaubt Änderung des Nachnamens
        if not name:
            raise ValueError("last_name is required")
        self.__last_name = name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str):
        # erlaubt Änderung der E-Mail
        if not value:
            raise ValueError("email is required")
        self.__email = value

    @property
    def address(self) -> Address:
        return self.__address

    @address.setter
    def address(self, address: Address):
        # setzt die Adresse neu (muss ein Address-Objekt sein)
        from model import Address
        if address is not None and not isinstance(address, Address):
            raise ValueError("address must be an instance of Address")
        self.__address = address

    @property
    def bookings(self) -> list[Booking]:
        # gibt eine Kopie der Buchungsliste zurück
        return self.__bookings.copy()

    def add_booking(self, booking: Booking):
        # fügt dem Gast eine Buchung hinzu, falls noch nicht vorhanden
        from model import Booking
        if not booking:
            raise ValueError("booking is required")
        if not isinstance(booking, Booking):
            raise ValueError("booking must be an instance of Booking")
        if booking not in self.__bookings:
            self.__bookings.append(booking)
            booking.guest = self  # setzt Rückverknüpfung im Booking-Objekt
