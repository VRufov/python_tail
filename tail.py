import os
import time

from pathlib import Path
from typing import BinaryIO

from parser import init_args_parser
from exceptions import IsNotFile, FileDeleted


def get_last_update(filepath: str):
    stats = os.stat(filepath)

    return stats.st_mtime


def is_file(filepath: str):
    return Path(filepath).is_file()


def is_file_exists(filepath: str):
    return Path(filepath).exists()


def check_file(filepath: str):
    if not is_file_exists(filepath):
        raise FileNotFoundError
    if not is_file(filepath):
        raise IsNotFile


def tail_observer(filename: str, lines: int):

    check_file(filename)
    last_update = get_last_update(filename)

    try:
        with open(filename, "rb") as file:
            print(tail(file=file, lines=lines))

            while True:
                new_update = get_last_update(filename)
                if last_update == new_update:
                    time.sleep(0.1)
                    continue

                print(tail(file, lines))
                last_update = new_update
    except FileNotFoundError:
        # Raises only when file has been renamed/moved/deleted
        raise FileDeleted


def tail(file: BinaryIO, lines: int) -> str:

    # Change the current file position to the end
    file.seek(0, 2)
    current_position = file.tell()

    block_size = 1024
    lines_found = 0
    block_number = -1
    blocks = []

    while lines_found < lines and current_position > 0:
        if current_position - block_size > 0:
            file.seek(block_number * block_size, 2)
            blocks.append(file.read(block_size))
        else:
            file.seek(0, os.SEEK_SET)
            blocks.append(file.read(current_position))

        lines_found += blocks[-1].count(b"\n")
        current_position -= block_size
        block_number -= 1

    all_read_text = b"".join(reversed(blocks))

    return b"\n".join(all_read_text.splitlines()[-lines:]).decode("utf-8")


if __name__ == "__main__":
    parser = init_args_parser()
    args = parser.parse_args()

    if args.follow:
        tail_observer(args.FILE, args.lines)
    else:
        check_file(args.FILE)
        with open(args.FILE, "rb") as file_obj:
            print(tail(file_obj, args.lines))
