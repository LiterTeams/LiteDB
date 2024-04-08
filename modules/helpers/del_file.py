from os import remove
from modules.helpers.find_file import find_file

# Global Variables

FF_FORMATS: set[str] = {"png", "jpg", "jpeg", "avif", "webp", "mp4", "avi", "webm", "json", "txt"}
FLN_PRIVATES: set[str] = {"modules", "venv", ".idea", ".git", "$WinREAgent", "edb", "OneDriveTemp", "OSPanel", "PerfLogs", "Program Files", "Program Files (x86)", "ProgramData", "temp", "Windows", "Users"}
FN_PRIVATES: set[str] = {"CON", "PRN", "AUX", "NUL", "COM", "LPT"}
SPEC_CHARS_PRIVATES: set[str] = {"#", "%", "&", "/", "«", "»", "<", ">", ":", "=", ","}
FF_REGEXP = f"{'|'.join(FF_FORMATS)}"
FN_REGEXP = f"{'|'.join(SPEC_CHARS_PRIVATES)}|{'|'.join(FN_PRIVATES)}"
FLN_REGEXP = f"{'|'.join(SPEC_CHARS_PRIVATES)}"
FF_TYPES = str | list[str] | set[str] | tuple[str] | None
FL_TYPES = str | list[str] | set[str] | tuple[str] | None


def del_file(fn: str | None = None, ff: str | None = None, fln_whitelist: FF_TYPES = None, fln_blacklist: FL_TYPES = None, fpath: str | None = None, rpath: str = "assets") -> None:
    r"""
    Supported Formats: png | jpg | jpeg | avif | webp | mp4 | avi | webm | json | txt
    :param fn: File name. If fpath is not specified, it is required.
    :param ff: File format. If fpath is not specified, it is required.
    :param fln_whitelist: Whitelist. List of folders to search for files. [optional]
    :param fln_blacklist: Blacklist. Ignores these folder name when searching for a folder. [optional]
    :param fpath: Full path to the file. This path must also include the file name and format. Not required if format and file name are specified.
    :param rpath: The root folder from which the file will be searched if the file format and name are specified.
    :return: dict - {size: int, unit: B | BT | KB | MB | GB | TB}
    """
    if all([fn, ff]):
        return remove(find_file(fn=fn, ff_whitelist=[ff], fln_whitelist=fln_whitelist, ff_blacklist=fln_blacklist, rpath=rpath)[0])
    if fpath:
        return remove(fpath)
