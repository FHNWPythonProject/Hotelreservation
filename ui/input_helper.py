def get_city_from_user():
    return input(" Bitte Stadt eingeben: ")

def get_min_stars_from_user() -> int:
    return int(input(" Bitte gewünschte Mindestanzahl Sterne eingeben: "))

def get_guest_count_from_user() -> int:
    return int(input(" Bitte Anzahl der Gäste eingeben: "))

def get_checkin_checkout_dates():
    from datetime import datetime
    checkin = input(" Check-in-Datum (YYYY-MM-DD): ")
    checkout = input(" Check-out-Datum (YYYY-MM-DD): ")
    return datetime.strptime(checkin, "%Y-%m-%d"), datetime.strptime(checkout, "%Y-%m-%d")

def get_hotel_name():
    return input(" Neuer Hotelname eingeben: ")

def get_street():
    return input(" Strasse: ")

def get_zip_code():
    return input(" PLZ: ")

def get_star_rating():
    return int(input(" Neue Anzahl Sterne (1–5): "))

def get_hotel_id_delete():
    return int(input(" Hotel-ID eingeben, das gelöscht werden soll: "))

def get_hotel_id():
    return int(input(" Hotel-ID eingeben, die bearbeitet werden soll: "))

def get_booking_id():
    return int(input(" Bitte geben Sie ihre Buchungs-ID ein: "))

def get_guest_full_info():
    first_name = input(" Vorname: ")
    last_name = input(" Nachname: ")
    email = input(" E-Mail-Adresse: ")
    return first_name, last_name, email

def get_room_type_description_from_user():
    return input(" Zimmertyp (z. B. Single, Double, Suite): ")
