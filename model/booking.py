class Booking:
    def __init__(self, booking_id: int, guest_id: int, room_id: int, checkin_date, checkout_date, total_amount: float, is_cancelled: bool, phone_number: str = None):
        self._booking_id = booking_id
        self._guest_id = guest_id
        self._room_id = room_id
        self._checkin_date = checkin_date
        self._checkout_date = checkout_date
        self._total_amount = total_amount
        self._is_cancelled = is_cancelled
        self._phone_number = phone_number  


    # ===================================
    # Getter + Setter für booking_id
    @property
    def booking_id(self):
        return self._booking_id

    @property
    def guest_id(self):
        return self._guest_id

    @property
    def room_id(self):
        return self._room_id

    @property
    def checkin_date(self):
        return self._checkin_date

    @checkin_date.setter
    def checkin_date(self, value):
        self._checkin_date = value

    @property
    def checkout_date(self):
        return self._checkout_date

    @checkout_date.setter
    def checkout_date(self, value):
        self._checkout_date = value

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    @property
    def is_cancelled(self):
        return self._is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, value):
        self._is_cancelled = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    

   


