from typing import List
from src.tcl_formatter.eol_slash_formatter import EolSlashFormatter
from src.core.apply_block_formatting import apply_block_formatting
import click

@click.command
@click.option("-f", "--filename")
@click.option("-r", "--range")
def format_my_code(filename: str, range: str = ""):
    """ Formats a .tcl file.
    
    Args:

        filename (str): Name of the file. ex: -f code.tcl

        range (str, optional): Ranges of lines to format. Defaults to all lines. ex: -r 20-30,40-50
    """
    lines = read_lines(filename)

    if range == "" or range is None:
        blocks = [[0, len(lines) - 1]]
    else:
        blocks = parse_user_specified_ranges(range)

    new_lines = apply_block_formatting(lines=lines, formatter=EolSlashFormatter, blocks_positions=blocks)
    write_lines(filename, new_lines)

def read_lines(filename: str) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

def write_lines(filename: str, lines: List[str]) -> None:
    file = open(filename, 'w')
    file.writelines(lines)
    file.close()

def parse_user_specified_ranges(range: str) -> List[List[int]]:
    """Parses user specified range to generate a usable list of ranges

    Args:
        range (str): user specified range(s) e.g. "5-10", "20-30,40-50"

    Returns:
        List[List[int]]: usable list of ranges e.g. [[4, 10]], [[19, 30], [39, 50]]
    """

    return [[int(single_range.split("-")[0]) - 1, int(single_range.split("-")[1])] for single_range in range.split(",")]
    
if __name__ == "__main__":
    format_my_code()
