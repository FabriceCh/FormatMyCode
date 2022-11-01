from typing import List
import os
import pytest

BASE_PATH = "tcl_formatters/test/test_data"
FORMATTED_PATH = os.path.join(BASE_PATH, "formatted/")
UNFORMATTED_PATH = os.path.join(BASE_PATH, "unformatted/")

def readlines(filename) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

@pytest.fixture(scope="session")
def unformatted_block() -> List[str]:
    return readlines(os.path.join(UNFORMATTED_PATH, "code_example_block.tcl"))

@pytest.fixture(scope="session")
def unformatted_code() -> List[str]:
    return readlines(os.path.join(UNFORMATTED_PATH, "code_example.tcl"))

@pytest.fixture(scope="session")
def formatted_block() -> List[str]:
    return readlines(os.path.join(FORMATTED_PATH, "code_example_block.tcl"))

@pytest.fixture(scope="session")
def formatted_code() -> List[str]:
    return readlines(os.path.join(FORMATTED_PATH, "code_example.tcl"))

@pytest.fixture(scope="session")
def unformatted_garchomp() -> List[str]:
    return readlines(os.path.join(UNFORMATTED_PATH, "garchomp.tcl"))

@pytest.fixture(scope="session")
def formatted_garchomp() -> List[str]:
    return readlines(os.path.join(FORMATTED_PATH, "garchomp.tcl"))
