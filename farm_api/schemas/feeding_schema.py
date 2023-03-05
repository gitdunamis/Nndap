from marshmallow import Schema, fields, post_load

class FeedingSchema(Schema):
    amount_kg = fields.Integer(attribute="feeding_amount_kg")
    cron_schedule = fields.String( attribute="feeding_cron_schedule")
    last_measured = fields.String(attribute="feeding_last_measured")
