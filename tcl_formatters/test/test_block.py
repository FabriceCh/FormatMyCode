from tcl_formatters.source.block import Block
from tcl_formatters.test.conftest import unformatted_block, formatted_block


def test_block_creation(unformatted_block):
    block = Block(unformatted_block)
    assert len(block.lines) == 4

def test_block_get_longest_line_length(unformatted_block):
    block = Block(unformatted_block)
    assert block._get_longest_line_length() == 22

def test_block_format(unformatted_block, formatted_block):
    block = Block(unformatted_block)
    for actual_line, expected_line in zip(block.format_lines(), formatted_block):
        assert actual_line == expected_line
