from typing import List

class Block:

    def __init__(self, lines: List[str], tab_size: int = 4) -> None:
        self.lines = lines
        self.tab_size = tab_size
        self.longest_line_length = self._get_longest_line_length()

    def _get_longest_line_length(self) -> int:
        max_len = 0
        for line in self.lines:
            apparent_len = self._get_apparent_line_length(line)
            if apparent_len > max_len:
                max_len = apparent_len
        return max_len

    def _get_apparent_line_length(self, line):
        n_tabs = line.count('\t')
        apparent_len = len(line) - n_tabs + n_tabs * self.tab_size
        return apparent_len

    def format_lines(self) -> List[str]:
        new_lines = []
        for line in self.lines:
            spaces_to_add = " " * (self.longest_line_length - self._get_apparent_line_length(line))
            new_line = line[:-2] + spaces_to_add + line[-2:]
            new_lines.append(new_line)
        return new_lines
