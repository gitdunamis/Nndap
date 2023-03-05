from marshmallow import Schema, fields, post_load

class MilkProductionSchema(Schema):
    last_milk = fields.String( attribute="milk_prod_last_milk")
    cron_schedule = fields.String( attribute="milk_prod_cron_schedule")
    amount_l = fields.Integer(attribute="milk_prod_amount_l")


