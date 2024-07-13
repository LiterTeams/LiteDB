from os import walk
import re

from modules.errors.FileNameError import FileNameError
from modules.errors.FormatError import FormatError
from modules.errors.FolderError import FolderError

from modules.helpers.find_directory import find_directory

# Global Variables

FF_FORMATS: set[str] = {"png", "jpg", "jpeg", "avif", "webp", "mp4", "avi", "webm", "json", "txt", "py"}
FLN_PRIVATES: set[str] = {"venv", ".idea", ".git", "$WinREAgent", "edb", "OneDriveTemp", "OSPanel", "PerfLogs", "Program Files", "Program Files (x86)", "ProgramData", "temp", "Windows", "Users"}
FN_PRIVATES: set[str] = {"CON", "PRN", "AUX", "NUL", "COM", "LPT"}
SPEC_CHARS_PRIVATES: set[str] = {"#", "%", "&", "/", "«", "»", "<", ">", ":", "=", ","}
FF_REGEXP = f"{'|'.join(FF_FORMATS)}"
FN_REGEXP = f"{'|'.join(SPEC_CHARS_PRIVATES)}|{'|'.join(FN_PRIVATES)}"
FLN_REGEXP = f"{'|'.join(SPEC_CHARS_PRIVATES)}"
FF_TYPES = str | list[str] | set[str] | tuple[str] | None
FL_TYPES = str | list[str] | set[str] | tuple[str] | None

def _convert_to_set(ff: FF_TYPES) -> set:
    match ff:
        case set(): return ff
        case list() | tuple(): return set(ff)
        case str(): return set(ff.split(sep=None))
        case _: return set()

def _global_handler(check_fn: bool = False, check_ff: bool = False, check_fln: bool = False, **kwargs) -> None:
    if check_fn and re.search(FN_REGEXP, kwargs["fn"], re.I): raise FileNameError("The file name contains invalid characters.")
    if check_ff and kwargs["ff_whitelist"].issubset(kwargs["ff_blacklist"]): raise FormatError("The white list of extension formats overlaps with the black list of extensions.")
    if check_ff and kwargs["ff_whitelist"].issubset(FF_FORMATS) & (kwargs["ff_blacklist"].issubset(FF_FORMATS) if kwargs["ff_blacklist"] else False) : raise FormatError("Your File Format or Blacklist contains an unsupported file format or is completely empty.")
    if check_fln and kwargs["fln_blacklist"].issubset(kwargs["fln_whitelist"]): raise FolderError("Elements of the white list of folders intersect with the black list of folders.")


def find_file(
        fn: str | None = None,
        ff_whitelist: FF_TYPES = None,
        ff_blacklist: FF_TYPES = None,
        fln_whitelist: FF_TYPES = None,
        fln_blacklist: FL_TYPES = None,
        folder_name: str | None = None,
        rpath: str = "assets",
        ppath: str | None = None,
        **kwargs
) -> str | list:
    r"""
    This function looks for a file inside your project.
    Supported Formats: png | jpg | jpeg | avif | webp | mp4 | avi | webm | json | txt
    If you do not specify a specific file extension in the white list, the first one that comes up will be returned.
    If there is more than 1 element in the whitelist of extensions, multiple searches are automatically triggered
    :param fn: File name. If you do not specify a file name, the file name is ignored. [+-required]
    :param ff_whitelist: Whitelist. Searches for files that match these formats. [optional]
    :param ff_blacklist: Blacklist. Ignores file extensions when searching for a file. [optional]
    :param fln_whitelist: Whitelist. List of folders to search for files. [optional]
    :param fln_blacklist: Blacklist. Ignores these folder name when searching for a folder. [optional]
    :param folder_name:  [optional]
    :param rpath: The root folder in which the file will be searched. [optional]
    :param ppath: Responds to searching for files in a specific project. [optional]
    :param kwargs:
        multiple_search: bool - Responsible for searching for files with different extensions, but with the same name. [optional],
        ignore_fn: bool - Ignores the file name when searching. should be used if you want to automatically search for files without a name, but with a specific extension. [optional]
    :return: list
    """

    formats_whitelist = _convert_to_set(ff_whitelist) if ff_whitelist else FF_FORMATS
    formats_blacklist = _convert_to_set(ff_blacklist) if ff_blacklist else set()
    folders_whitelist = _convert_to_set(fln_whitelist) if fln_whitelist else set()
    folders_blacklist = _convert_to_set(fln_blacklist) | FLN_PRIVATES if fln_blacklist else FLN_PRIVATES

    multiple_search = kwargs.get("multiple_search", False)
    ignore_fn = kwargs.get("ignore_fn", False)

    if len(formats_whitelist) > 1 or not fn: multiple_search = True
    if not fn or len(fn) == 0: ignore_fn = True

    _global_handler(check_fn=False if ignore_fn else True, **{"fn": fn})
    _global_handler(check_ff=True, **{"ff_whitelist": formats_whitelist, "ff_blacklist": formats_blacklist})
    _global_handler(check_fln=True, **{"fln_whitelist": folders_whitelist, "fln_blacklist": folders_blacklist})

    ff_whitelist_regexp = "|".join(formats_whitelist.difference(formats_blacklist))
    my_files = set(f"{fn}.{fl_format}" for fl_format in formats_whitelist) if not ignore_fn else set()

    if multiple_search:
        searched_files = []
        for root, dist, files in walk(find_directory(folder_name=folder_name or rpath, base_directory=ppath, rpath=rpath)):
            if not set(root.split("\\")) & folders_blacklist and files:
                if ignore_fn:
                    for file in files:
                        if re.search(ff_whitelist_regexp, file, re.I):
                            searched_files.append(f"{root}\\{file}")
                else:
                    for file in list(set(files) & my_files):
                        searched_files.append(f"{root}\\{file}")
        return searched_files

    for root, dist, files in walk(find_directory(folder_name=folder_name or rpath, base_directory=ppath, rpath=rpath)):
        if not set(root.split("\\")) & folders_blacklist and files:
            for file in list(set(files) & my_files if not ignore_fn else set(files)):
                return f"{root}\\{file}"
