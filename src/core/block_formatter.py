from abc import ABC
from typing import List

class BlockFormatter(ABC):
    @staticmethod
    def format_block(lines: List[str]) -> List[str]:
        return []
