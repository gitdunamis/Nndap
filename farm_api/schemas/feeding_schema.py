from marshmallow import Schema, fields, post_load
import json_fix

class FeedingSchema(object):
    amount_kg : int  #= fields.Integer(attribute="feeding_amount_kg")
    cron_schedule: str #  = fields.String( attribute="feeding_cron_schedule")
    last_measured: str # = fields.String(attribute="feeding_last_measured")

    def __json__(self) :
        return self.__dict__


