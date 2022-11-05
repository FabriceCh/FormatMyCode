from typing import List
from src.core.block_formatter import BlockFormatter

class EolSlashBLockFormatter(BlockFormatter):

    TAB_SIZE = 4

    @staticmethod
    def _get_longest_line_length(lines) -> int:
        max_len = 0
        for line in lines:
            apparent_len = EolSlashBLockFormatter._get_apparent_line_length(line)
            if apparent_len > max_len:
                max_len = apparent_len
        return max_len

    @staticmethod
    def _get_apparent_line_length(line):
        n_tabs = line.count('\t')
        apparent_len = len(line) - n_tabs + n_tabs * EolSlashBLockFormatter.TAB_SIZE
        return apparent_len

    @staticmethod
    def format_block(lines) -> List[str]:
        new_lines = []
        longest_line_length = EolSlashBLockFormatter._get_longest_line_length(lines)
        for line in lines:
            spaces_to_add = " " * (longest_line_length - EolSlashBLockFormatter._get_apparent_line_length(line))
            new_line = line[:-2] + spaces_to_add + line[-2:]
            new_lines.append(new_line)
        return new_lines
