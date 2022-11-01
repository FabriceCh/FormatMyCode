from typing import List
from src.tcl_formatter.eol_slash_formatter import EolSlashFormatter
import click

@click.command
@click.option("-f", "--filename")
def format_my_code(filename: str):
    lines = read_lines(filename)
    new_lines = EolSlashFormatter.format_block(lines)
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
