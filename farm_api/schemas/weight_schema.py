import datetime

class WeightSchema(object):
    mass_kg : int
    last_measured : datetime


    def __json__(self) :
        return self.__dict__

