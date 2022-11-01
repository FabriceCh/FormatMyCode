from typing import List
from src.tcl_formatter.align_slashes import format_lines
import click

@click.command
@click.option("-f", "--filename")
def format_my_code(filename: str):
    lines = read_lines(filename)
    new_lines = format_lines(lines)
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


if __name__ == "__main__":
    format_my_code()
