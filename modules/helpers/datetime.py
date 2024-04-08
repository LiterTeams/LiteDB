from DateTime import DateTime

def _date_format_current() -> str:
    date = str(DateTime.date.today()).split("-")
    return f"{date[2]}-{date[1]}-{date[0]}"


def _time_format_current() -> str:
    time = str(DateTime.datetime.now().time()).split(".")[0].split(":")
    return f"{int(time[0])}:{time[1]} {'am' if 0 <= int(time[0]) <= 11 else 'pm'}"


def _datetime_format_current() -> str:
    date = _date_format_current()
    time = _time_format_current()
    return f"{date} | {time}"


def date_format(date_type: str) -> str:
    if date_type == "date()":
        return _date_format_current()
    elif date_type == "time()":
        return _time_format_current()
    elif date_type == "datetime()":
        return _datetime_format_current()
    return "null"
