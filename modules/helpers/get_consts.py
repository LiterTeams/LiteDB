
def get_consts(values: dict) -> list:
    consts = []
    for key, value in values.items():
        if "const" in value: consts.append(key)
    return consts
