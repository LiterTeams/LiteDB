
def get_relations(values: dict) -> list:
    relations = []
    for key, value in values.items():
        if "relation" in value:
            value = value.split("|")
            for i in value:
                if i.startswith("relation"):
                    i = i.split("relation:")[1].split("[")[1].split("]")[0].split(":")
                    relations.append({"attribute": key, "table": i[0], "fields": i[1]})
    return relations
