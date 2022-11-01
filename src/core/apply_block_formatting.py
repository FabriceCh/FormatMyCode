from typing import List
from src.core.block_formatter import BlockFormatter
from typing import Type

def apply_block_formatting(lines: List[str], formatter: Type[BlockFormatter], blocks_positions: List[List[int]]):
    new_lines = []
    line_cursor = 0
    for block_position in blocks_positions:
        start, end = block_position[0], block_position[1]
        new_lines += lines[line_cursor:start]
        block = lines[start:end]
        new_lines += formatter.format_block(block)
        line_cursor = end
    new_lines += lines[line_cursor:]
    return new_lines
