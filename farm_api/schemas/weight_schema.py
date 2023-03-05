from marshmallow import Schema, fields, post_load

class WeightSchema(Schema):
    mass_kg = fields.Integer(attribute="weight_mass_kg")
    last_measured = fields.String( attribute="weight_last_measured")
