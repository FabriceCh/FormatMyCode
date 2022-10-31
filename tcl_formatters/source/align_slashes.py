from typing import List
import click

@click.command
@click.option("-f", "--filename")
def align_slashes(filename: str):
    lines = read_lines(filename)
    for i, line in enumerate(lines):
        if line.endswith('\\\n'):
            print(i)

def read_lines(filename: str) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

def find_blocks(lines):
    blocks


if __name__ == "__main__":
    align_slashes()
