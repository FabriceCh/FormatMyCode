from typing import List

class Block:

    def __init__(self, lines: List[str]) -> None:
        self.lines = lines

    def _get_longest_line_length(self) -> int:
        max_len = 0
        for line in self.lines:
            if len(line) > max_len:
                max_len = len(line)
        return max_len

    def format_lines(self) -> List[str]:
        return self.lines
