class Address:
    def __init__(self, address_id: int, street: str, city: str, zip_code: str):
        if not isinstance(address_id, int):
            raise ValueError("address_id must be an integer")
        if not street:
            raise ValueError("street is required")
        if not city:
            raise ValueError("city is required")
        if not zip_code:
            raise ValueError("zip_code is required")

        self.__address_id = address_id
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code

    def __repr__(self):
        return f"Address(id={self.__address_id}, street={self.__street}, city={self.__city}, zip_code={self.__zip_code})"

    @property
    def address_id(self) -> int:
        return self.__address_id

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        if not street:
            raise ValueError("street cannot be empty")
        self.__street = street

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        if not city:
            raise ValueError("city cannot be empty")
        self.__city = city

    @property
    def zip_code(self) -> str:  # ✅ Richtiger Property-Name!
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, zip_code: str):  # ✅ ebenfalls konsistent
        if not zip_code:
            raise ValueError("zip_code cannot be empty")
        self.__zip_code = zip_code
