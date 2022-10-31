from typing import List
import pytest


def readlines(filename) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

@pytest.fixture(scope="session")
def raw_block() -> List[str]:
    return readlines("/home/fab/repos/FormatMyCode/tcl_formatters/test_data/code_example_block.tcl")