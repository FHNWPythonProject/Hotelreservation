def get_city_from_user():
    return input("🏙️ Bitte Stadt eingeben: ")

def get_min_stars_from_user() -> int:
    return int(input("⭐ Bitte gewünschte Mindestanzahl Sterne eingeben: "))

def get_guest_count_from_user() -> int:
    return int(input("👥 Bitte Anzahl der Gäste eingeben: "))

def get_checkin_checkout_dates():
    from datetime import datetime
    checkin = input("📅 Check-in-Datum (YYYY-MM-DD): ")
    checkout = input("📅 Check-out-Datum (YYYY-MM-DD): ")
    return datetime.strptime(checkin, "%Y-%m-%d"), datetime.strptime(checkout, "%Y-%m-%d")

def get_hotel_name():
    return input(" Hotelname eingeben: ")

def get_street():
    return input(" Strasse: ")

def get_zip_code():
    return input(" PLZ: ")

def get_star_rating():
    return int(input("⭐ Anzahl Sterne (1–5): "))