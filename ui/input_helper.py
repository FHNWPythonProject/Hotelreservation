def get_city_from_user():
    city = input("Bitte Stadt eingeben: ")
    return city.capitalize()

def get_min_stars_from_user() -> int:
    while True:
        value = input(" Bitte gewünschte Mindestanzahl Sterne eingeben (1–5): ")
        if not value.isdigit():
            print(" Ungültige Eingabe. Bitte eine Zahl eingeben.")
            continue

        value = int(value)
        if value < 1 or value > 5:
            print(" Die Anzahl Sterne muss zwischen 1 und 5 liegen.")
            continue

        return value

def get_guest_count_from_user() -> int:
    while True:
        value = input(" Bitte Anzahl der Gäste eingeben: ")
        if not value.isdigit():
            print(" Ungültige Eingabe. Bitte eine Zahl eingeben.")
            continue

        value = int(value)
        if value <= 0:
            print(" Die Anzahl der Gäste muss mindestens 1 sein.")
            continue

        return value


def get_checkin_checkout_dates():
    from datetime import datetime

    while True:
        try:
            checkin_str = input("Check-in-Datum (YYYY-MM-DD): ")
            checkin = datetime.strptime(checkin_str, "%Y-%m-%d")
            
            checkout_str = input("Check-out-Datum (YYYY-MM-DD): ")
            checkout = datetime.strptime(checkout_str, "%Y-%m-%d")
            
            if checkout <= checkin:
                print("Fehler: Check-out-Datum muss nach dem Check-in-Datum liegen.")
                continue
            
            return checkin, checkout

        except ValueError:
            print("Fehler: Bitte gib das Datum im Format YYYY-MM-DD ein.")


def get_hotel_name():
    return input(" Neuer Hotelname eingeben: ")

def get_street():
    return input(" Strasse: ")

def get_zip_code():
    while True:
        value = input(" PLZ (4-stellig): ")
        if not value.isdigit():
            print(" Ungültige Eingabe. Bitte nur Ziffern eingeben.")
            continue
        if len(value) != 4:
            print(" Die PLZ muss genau 4 Ziffern haben.")
            continue
        return int(value)


def get_star_rating():
    while True:
        value = input(" Neue Anzahl Sterne (1–5): ")
        if not value.isdigit():
            print(" Ungültige Eingabe. Bitte eine Zahl eingeben.")
            continue
        value = int(value)
        if value < 1 or value > 5:
            print(" Anzahl Sterne muss zwischen 1 und 5 liegen.")
            continue
        return value


def get_hotel_id_delete():
    while True:
        value = input(" Hotel-ID eingeben, das gelöscht werden soll: ")
        if not value.isdigit():
            print(" Ungültige Eingabe. Bitte eine Zahl eingeben.")
            continue
        value = int(value)
        if value <= 0:
            print(" Hotel-ID muss größer als 0 sein.")
            continue
        return value


def get_hotel_id():
    while True:
        value = input(" Hotel-ID eingeben, die bearbeitet werden soll: ")
        if not value.isdigit():
            print(" Ungültige Eingabe. Bitte eine Zahl eingeben.")
            continue
        value = int(value)
        if value <= 0:
            print(" Hotel-ID muss größer als 0 sein.")
            continue
        return value


def get_booking_id():
    while True:
        value = input(" Bitte geben Sie ihre Buchungs-ID ein: ")
        if not value.isdigit():
            print(" Ungültige Eingabe. Bitte eine Zahl eingeben.")
            continue
        value = int(value)
        if value <= 0:
            print(" Buchungs-ID muss größer als 0 sein.")
            continue
        return value


def get_guest_full_info():
    first_name = input(" Vorname: ")
    last_name = input(" Nachname: ")
    email = input(" E-Mail-Adresse: ")
    return first_name, last_name, email

def get_room_type_description_from_user():
    return input(" Zimmertyp (z. B. Single, Double, Suite): ")
