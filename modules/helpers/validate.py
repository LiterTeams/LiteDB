
def empty_check(): ...

def quantity_check(): ...

def length_check(): ...

def type_check(value: str | int, type_default: str) -> bool:
    match type_default:
        case "int": return type(value) is int
        case "str": return type(value) is str
        case "float": return type(value) is float
        case "list": return type(value) is list
        case "dict": return type(value) is dict
        case "tuple": return type(value) is tuple
    return False

def enum_check(value: str, enum: str) -> bool:
    enum = enum.split("|")
    enum = ",".join([i.split("enum")[1].split("[")[1].split("]")[0] for i in enum if i.startswith("enum")]).split(",")
    return value in enum
