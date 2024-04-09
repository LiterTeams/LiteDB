from DateTime import DateTime

def _date_format_current() -> str:
    date = DateTime().Date().split("/")
    return f"{date[2]}-{date[1]}-{date[0]}"


def _time_format_current() -> str:
    time = DateTime().AMPM().split(":")
    return f"{int(time[0])}:{time[1]} {time[-1].split(' ')[1]}"


def _datetime_format_current() -> str:
    date = _date_format_current()
    time = _time_format_current()
    return f"{date} | {time}"


def datetime(date_type: str) -> str:
    match date_type:
        case "date": return _date_format_current()
        case "time": return _time_format_current()
        case "datetime": return _datetime_format_current()
        case _: return "null"
