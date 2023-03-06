from farm_api.models.cow import Cow
import json



class CowSchema(object):
    """
    Schema used for loading/dumping Cows
    """
    cow_id : int
    name : str
    sex : str
    birthdate : str
    condition : str
    weight  = None
    feeding = None
    milk_production = None
    has_calves : bool

    def dump(self):
        return self.__dict__
