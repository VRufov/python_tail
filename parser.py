from argparse import ArgumentParser


def init_args_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument(
        "-f",
        "--follow",
        help="output appended data as the file grows",
        required=False,
        action="store_true",
    )
    parser.add_argument(
        "-n",
        "--lines",
        type=int,
        help="output the last NUM lines, instead of the last 10",
        default=10,
        required=False,
    )
    parser.add_argument(
        "FILE",
        type=str,
        help="File name to read",
    )

    return parser
