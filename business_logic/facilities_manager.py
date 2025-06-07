from data_access.facilities_dal import FacilitiesDAL

class FacilitiesManager:
    def __init__(self):
        self.facilities_dal = FacilitiesDAL()

    def create_facilities(self, description: str):
        return self.facilities_dal.create_facilities(description)