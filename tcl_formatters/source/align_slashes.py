from typing import List
import click
from tcl_formatters.source.block import Block

@click.command
@click.option("-f", "--filename")
def align_slashes(filename: str):
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

def find_blocks_positions(lines):
    current_block_start = None
    blocks_positions = []
    for i, line in enumerate(lines):
        if line.endswith('\\\n'):
            if current_block_start is None:
                current_block_start = i
            else:
                continue
        else:
            if current_block_start is not None:
                blocks_positions.append([current_block_start, i])
                current_block_start = None
            else:
                continue
    return blocks_positions

def format_lines(lines):
    blocks_positions = find_blocks_positions(lines)
    new_lines = []
    line_cursor = 0
    for block_position in blocks_positions:
        start, end = block_position[0], block_position[1]

        new_lines += lines[line_cursor:start]
        block = Block(lines[start:end])
        new_lines += block.format_lines()
        
        line_cursor = end
    new_lines += lines[line_cursor:]
    return new_lines


if __name__ == "__main__":
    align_slashes()
