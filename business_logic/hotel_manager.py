import pandas as pd
from data_access.hotel_dal import HotelDAL

from model.hotel import Hotel

class HotelManager:
    def __init__(self):
        self.__hotel_dal = data_access.HotelDAL()

    def read_all_hotels_as_df(self) -> pd.DataFrame:
        # Liefert alle Hotels aus der Datenbank als Pandas DataFrame zurück, geeignet für Anzeige, Filterung oder Weiterverarbeitung.
        return self.__hotel_dal.read_all_hotels_as_df()

    def get_hotels_by_city(self, city: str) -> list[Hotel]:
        # Gibt alle Hotels in der angegebenen Stadt zurück.
        return self._hotel_dal.read_hotels_by_city(city)

