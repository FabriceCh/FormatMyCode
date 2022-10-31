from tcl_formatters.source.block import Block
from tcl_formatters.test.conftest import raw_block


def test_block_get_longest_line_length(raw_block):
    block = Block(raw_block)
    assert block._get_longest_line_length() == 22
