from pathlib import Path

def camp_cleanup():
    return

def read_file(file_name):
    file = Path(file_name)
    if Path.is_file(file):
        return Path.read_text(file)
    else:
        raise TypeError("This is not a file")