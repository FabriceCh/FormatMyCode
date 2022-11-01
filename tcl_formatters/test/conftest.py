from typing import List
import pytest


def readlines(filename) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

@pytest.fixture(scope="session")
def unformatted_block() -> List[str]:
    return readlines("./tcl_formatters/test_data/unformatted/code_example_block.tcl")

@pytest.fixture(scope="session")
def unformatted_code() -> List[str]:
    return readlines("./tcl_formatters/test_data/unformatted/code_example.tcl")

@pytest.fixture(scope="session")
def formatted_block() -> List[str]:
    return readlines("./tcl_formatters/test_data/formatted/code_example_block.tcl")

@pytest.fixture(scope="session")
def formatted_code() -> List[str]:
    return readlines("./tcl_formatters/test_data/formatted/code_example.tcl")


@pytest.fixture(scope="session")
def unformatted_garchomp() -> List[str]:
    return readlines("./tcl_formatters/test_data/unformatted/garchomp.tcl")

@pytest.fixture(scope="session")
def formatted_garchomp() -> List[str]:
    return readlines("./tcl_formatters/test_data/formatted/garchomp.tcl")
