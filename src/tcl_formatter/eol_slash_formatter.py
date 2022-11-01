from typing import List
from src.tcl_formatter.eol_slash_block_formatter import EolSlashBLockFormatter
from src.core.apply_block_formatting import apply_block_formatting
from src.core.block_formatter import BlockFormatter


class EolSlashFormatter(BlockFormatter):

    @staticmethod
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

    @staticmethod
    def format_block(lines: List[str]):
        blocks_positions = EolSlashFormatter.find_blocks_positions(lines)
        new_lines = apply_block_formatting(lines, EolSlashBLockFormatter, blocks_positions)
        return new_lines

