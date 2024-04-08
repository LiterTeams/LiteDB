
def get_defaults(values: dict) -> list:
    defaults = []
    for key, value in values.items():
        if "auto" in value or "default" in value: defaults.append(key)
    return defaults
