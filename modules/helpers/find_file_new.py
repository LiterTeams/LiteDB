from os import walk
from os.path import abspath

FF_FORMATS: set[str] = {"png", "jpg", "jpeg", "avif", "webp", "mp4", "avi", "webm", "json", "txt"}

def _convert_to_set(ff: set | list | str) -> set:
    match ff:
        case set(): return ff
        case list() | tuple(): return set(ff)
        case str(): return set(ff.split(sep=None))
        case _: return set()

def _find_directory(rpath: str = "assets"): ...

def _alias(folder_name: str, rpath: str | None = None):
    for root, dist, files in walk(abspath(rpath)):
        if folder_name in set(root.split("\\")): return root

def find_file(
        fn_ignore: list | str | None = None,
        ff_whitelist: list | str | None = None,
        fln_whitelist: list | str | None = None,
        rpath: str = "assets"
) -> list[dict]:
    searched_files = []
    fn_ignore = _convert_to_set(fn_ignore) # {Models}
    ff_whitelist = _convert_to_set(ff_whitelist) # {py}
    fln_whitelist = _convert_to_set(fln_whitelist) # {models}
    for folder in fln_whitelist:
        res = _alias(folder, rpath)
        if res:
            for root, dist, files in walk(res):
                for file in files:
                    file = file.split(".")
                    file_name = file[0]
                    file_type = file[1]
                    if file_type in ff_whitelist and file_name not in fn_ignore:
                        searched_files.append({"name": file_name, "format": file_type, "path": f"{root}"})

    return searched_files
