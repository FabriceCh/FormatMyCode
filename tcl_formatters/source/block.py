from typing import List

class Block:

    def __init__(self, lines: List[str]) -> None:
        self.lines = lines
        self.longest_line_length = self._get_longest_line_length()

    def _get_longest_line_length(self) -> int:
        max_len = 0
        for line in self.lines:
            if len(line) > max_len:
                max_len = len(line)
        return max_len

    def format_lines(self) -> List[str]:
        new_lines = []
        for line in self.lines:
            spaces_to_add = " " * (self.longest_line_length - len(line))
            new_line = line[:-2] + spaces_to_add + line[-2:]
            new_lines.append(new_line)
        return new_lines
