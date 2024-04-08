from modules.helpers.find_file import find_file

# Global Variables

FF_TYPES = str | list[str] | set[str] | tuple[str] | None
FL_TYPES = str | list[str] | set[str] | tuple[str] | None

def auto_search_files(
        ff_whitelist: FF_TYPES = None,
        ff_blacklist: FF_TYPES = None,
        fln_whitelist: FF_TYPES = None,
        fln_blacklist: FL_TYPES = None,
        folder_name: str | None = None,
        root_path: str = "assets",
        project_path: str = "current"
):
    r"""
    This function looks for a file inside your project.
    Supported Formats: png | jpg | jpeg | avif | webp | mp4 | avi | webm | json | txt
    *To avoid a long search, it is advisable to specify the root directory as accurately as possible.
    :param ff_whitelist: Whitelist. Searches for files that match these formats. [optional]
    :param ff_blacklist: Blacklist. Ignores file extensions when searching for a file. [optional]
    :param fln_whitelist: Whitelist. List of folders to search for files. [optional]
    :param fln_blacklist: Blacklist. Ignores these folder name when searching for a folder. [optional]
    :param root_path: The root folder in which the file will be searched. [optional]
    :param project_path: Responds to searching for files in a specific project. [optional]
    :return: [{name:..., format:...}...]
    """
    searched_files = find_file(ff_whitelist=ff_whitelist, ff_blacklist=ff_blacklist, fln_whitelist=fln_whitelist, fln_blacklist=fln_blacklist, folder_name=folder_name, rpath=root_path, ppath=project_path, **{"ignore_fn": True})
    return [{"name": "".join(file.split(".")[0].split("\\")[-1]), "format": file.split(".")[-1]} for file in searched_files]
