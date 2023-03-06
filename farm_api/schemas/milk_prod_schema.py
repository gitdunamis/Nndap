import json_fix

class MilkProductionSchema(object):
    last_milk : str
    cron_schedule : str
    amount_l : int

    
    def __json__(self) :
        return self.__dict__



