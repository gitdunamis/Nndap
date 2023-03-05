from marshmallow import Schema, fields, post_load
from farm_api.models.cow import Cow
# from farm_api.schemas.weight_schema import WeightSchema
# from farm_api.schemas.feeding_schema import FeedingSchema
# from farm_api.schemas.milk_prod_schema import MilkProductionSchema
# from farm_api.schemas.self_nested import SelfNested, NamespacedSchema, NamespaceOpts
# from farm_api.database import db
import json


class CowSchema(object):
    """
    Cow Marshmallow Schema

    Marshmallow schema used for loading/dumping Cows
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
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

# class Object:
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__, 
#             sort_keys=True, indent=4)

    # cow_id = fields.Integer()
    # name = fields.String()
    # sex = fields.String()
    # birthdate = fields.String()
    # condition = fields.String()
    # weight = fields.Nested(WeightSchema())
    # feeding = fields.Nested(FeedingSchema())
    # milk_production = fields.Nested(MilkProductionSchema())
    # has_calves = fields.Bool()

    # @post_load
    # def make_cow(self, data, **kwargs):
    #     return data
        # new_cow = Cow()
        # new_cow.birthdate = data['birthdate']
        # new_cow.name = data['name']
        # new_cow.has_calves = data['has_calves']
        # new_cow.condition = data['condition']
        # new_cow.sex = data['sex']
        # new_cow.milk_prod_amount_l = data['milk_production']['milk_prod_amount_l']
        # new_cow.milk_prod_last_milk = data['milk_production']['milk_prod_last_milk']
        # new_cow.milk_prod_cron_schedule = data['milk_production']['milk_prod_cron_schedule']
        # new_cow.weight_last_measured = data['weight']['weight_last_measured']
        # new_cow.weight_mass_kg = data['weight']['weight_mass_kg']
        # new_cow.feeding_cron_schedule = data['feeding']['feeding_cron_schedule']
        # new_cow.feeding_last_measured = data['feeding']['feeding_last_measured']
        # new_cow.feeding_amount_kg = data['feeding']['feeding_amount_kg']

        # return new_cow

    # feeding_amount_kg = fields.Integer()
    # feeding_cron_schedule = fields.String()
    # feeding_last_measured = fields.String()
    # milk_prod_last_milk = fields.String()
    # milk_prod_cron_schedule = fields.String()
    # milk_prod_amount_l = fields.Integer()
    # weight_mass_kg = fields.Integer()
    # weight_last_measured = fields.String()


   