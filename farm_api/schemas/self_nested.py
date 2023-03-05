from marshmallow import Schema, fields, SchemaOpts, pre_load, post_dump
from marshmallow.utils import missing


class SelfNested(fields.Nested):
    def get_value(self, obj, attr, accessor=None, default=missing):
        return obj


class NamespaceOpts(SchemaOpts):
    """Same as the default class Meta options, but adds "name" and
    "plural_name" options for enveloping.
    """

    def __init__(self, meta, **kwargs):
        SchemaOpts.__init__(self, meta, **kwargs)
        self.name = getattr(meta, "name", None)
        self.plural_name = getattr(meta, "plural_name", self.name)

class NamespacedSchema(Schema):
    OPTIONS_CLASS = NamespaceOpts

    @pre_load(pass_many=True)
    def unwrap_envelope(self, data, many, **kwargs):
        key = self.opts.plural_name if many else self.opts.name
        return data[key]

    @post_dump(pass_many=True)
    def wrap_with_envelope(self, data, many, **kwargs):
        key = self.opts.plural_name if many else self.opts.name
        return {key: data}


def identity_accessor(attr, obj, default):
    return obj or default


class Section(fields.Nested):
    def get_value(self, attr, obj, accessor=None, default=missing):
        return super(Section, self).get_value(attr, obj,
                                              accessor=identity_accessor,
                                              default=default)