
sys_keys = {"minmax", "required"}

def get_keys(values: dict) -> list:
    keys = []
    for key, value in values.items():
        if "minmax" in value or "required" in value: keys.append(key)
    return keys
