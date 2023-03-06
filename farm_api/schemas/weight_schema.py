from marshmallow import Schema, fields, post_load

class WeightSchema(object):
    mass_kg = fields.Integer(attribute="weight_mass_kg")
    last_measured = fields.String( attribute="weight_last_measured")


    def __json__(self) :
        return self.__dict__

