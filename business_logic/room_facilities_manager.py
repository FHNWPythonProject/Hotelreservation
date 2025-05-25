from data_access.facilities_dal import FacilitiesDAL

class FacilityManager:
    def __init__(self):
        self.facility_dal = FacilitiesDAL()

    def create_facility(self, description: str):
        return self.facility_dal.create_facility(description)