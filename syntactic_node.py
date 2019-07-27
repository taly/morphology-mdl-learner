class SyntacticNode:

    TYPE_ROOT = "TYPE_ROOT"
    TYPE_FEATURE = "TYPE_FEATURE"

    def __init__(self, type, repr, encoding, surface_form=None):
        self.type = type
        self.repr = repr
        self.encoding = encoding
        self.surface_form = surface_form

    def get_encoding_length(self):
        return len(repr(self.encoding))

    def __hash__(self):
        return hash(self.repr)

    def __repr__(self):
        return self.repr

    def __eq__(self, other):
        return self.type == other.type and self.repr == other.repr and self.encoding == other.encoding
