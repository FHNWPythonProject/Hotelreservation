from datetime import date, datetime
import sqlite3

def date_to_db(d: date) -> str:
    return d.isoformat()

def db_to_date(s: str) -> date:
    return datetime.strptime(s.decode(), "%Y-%m-%d").date()

## Adapter: Wandelt `date`-Objekt in `TEXT` um
sqlite3.register_adapter(date, date_to_db)
## Konverter: Wandelt gespeicherte `TEXT`-Werte wieder in `date`
sqlite3.register_converter("DATE", db_to_date)

from data_access.address_dal import AddressDAL

from .hotel_dal import HotelDAL
from .guest_dal import GuestDAL
from .room_dal import RoomDAL
from .room_type_dal import RoomTypeDAL
from .booking_dal import BookingDAL
from .invoice_dal import InvoiceDAL
from .facilities_dal import FacilitiesDAL
from .room_facilities_dal import RoomFacilitiesDAL
from .address_dal import AddressDAL
from .base_dal import BaseDal  # falls benötigt
