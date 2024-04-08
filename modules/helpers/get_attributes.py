
sys_types = {"any", "int", "str", "dict", "list", "set", "tuple", "enum", "null"}
sys_attributes = {"const", "auto", "required"}

def get_attributes(values: dict) -> dict:
    attributes = dict()
    for key, value in values.items():
        attrs = set(value.split("|")).difference(sys_types).difference(sys_attributes)
        attributes[key] = "|".join(str(attr) for attr in attrs)
    return attributes
