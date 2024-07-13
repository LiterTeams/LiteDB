from math import ceil
from random import randint


def get_by_id(data: list[dict], id: int) -> dict:
    result = list(filter(lambda data_item: data_item.get("id") == id, data))
    return result[0] if len(result) == 1 else dict()

def get_by_search(data: list[dict], search: str) -> dict:
    ...

def order_by_filter(data: list[dict], params: dict) -> dict:
    temp_data = list()
    response = {"data": data, "meta": {"pages": 1, "items": 0, "total_items": 0}}
    for key, value in params.items():
        match value:
            case "asc": break
            case "desc": ...
    return response

def random(data: list[dict], limit: int) -> dict:
    limit = limit if limit > len(data) | limit < len(data) else len(data)
    response = {"data": list(), "meta": {"pages": 1, "items": 0, "total_items": 0}}
    for i in range(limit):
        if len(data) == 1:
            response.get("data").append(data.pop())
            break
        else:
            response.get("data").append(data.pop(randint(0, len(data) - 1)))
    items = len(response.get("data"))
    response.get("meta").update(items=items, total_items=items)
    return response

def paginating(data, limit: int) -> dict:
    response = {"data": [], "meta": {"pages": 1, "items": 0, "total_items": 0}}
    if limit <= 0: return data
    for index, data_item in enumerate(data, start=1):
        if index > limit: break
        response.get("data").append(data_item)

    items = len(response.get("data"))
    total_items = len(data)
    pages = ceil(total_items / items)
    response.get("meta").update(pages=pages, items=items, total_items=total_items)

    return response
