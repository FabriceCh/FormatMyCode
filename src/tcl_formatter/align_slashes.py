from typing import List
from src.tcl_formatter.block import Block

def find_blocks_positions(lines: List[str]):
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

def format_lines(lines: List[str]):
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

