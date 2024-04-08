
sys_types = {"any", "int", "str", "dict", "list", "set", "tuple", "enum", "null"}

def get_types(values: dict) -> dict:
    types = dict()
    for key, value in values.items():
        type_value = set(value.split("|")) & sys_types
        if type_value: types[key] = "".join(str(elem) for elem in type_value)
    return types


