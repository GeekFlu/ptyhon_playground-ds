import os
from os.path import join


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain fur ther subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix is None or path is None:
        return []
    if suffix.isspace() or path.isspace():
        return []
    if len(suffix) <= 0 or len(path) <= 0:
        return []
    keep_digging = True
    files = []
    dirs = [path]
    while keep_digging:
        if len(dirs) > 0:
            cur_path = dirs.pop()
            try:
                for e in os.listdir(cur_path):
                    current_file = join(cur_path, e)
                    if os.path.isfile(current_file) and e.endswith(suffix):
                        files.append(current_file)
                    elif os.path.isdir(current_file):
                        dirs.append(current_file)
            except FileNotFoundError as error:
                break
        else:
            break

    return files


if __name__ == "__main__":
    print(find_files(".c", "./testdir"))
    print(find_files(".py", "./testdir"))
