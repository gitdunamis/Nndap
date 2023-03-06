
class WeightSchema(object):
    mass_kg : int
    last_measured : str


    def __json__(self) :
        return self.__dict__

