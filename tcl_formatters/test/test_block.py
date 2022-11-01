from tcl_formatters.source.block import Block
from tcl_formatters.source.align_slashes import find_blocks_positions, format_lines


def test_block_creation(unformatted_block):
    block = Block(unformatted_block)
    assert len(block.lines) == 4

def test_block_get_longest_line_length_single():
    block = Block(["\t\tcode \\\n"])
    assert block._get_longest_line_length() == 15

def test_block_get_longest_line_length(unformatted_block):
    block = Block(unformatted_block)
    assert block._get_longest_line_length() == 32

def test_block_format(unformatted_block, formatted_block):
    block = Block(unformatted_block)
    for actual_line, expected_line in zip(block.format_lines(), formatted_block):
        assert actual_line == expected_line
    
def test_find_blocks_positions(unformatted_code, unformatted_garchomp):
    blocks_positions = find_blocks_positions(unformatted_code)
    blocks_positions_garchomp = find_blocks_positions(unformatted_garchomp)
    assert blocks_positions == [[4, 8], [14, 20]]
    assert blocks_positions_garchomp == [[0, 4], [5, 14], [15, 16]]

def test_format_file(unformatted_code, formatted_code):
    actual = format_lines(unformatted_code)
    assert actual == formatted_code

def test_format_file_garchomp(unformatted_garchomp, formatted_garchomp):
    actual = format_lines(unformatted_garchomp)
    assert actual == formatted_garchomp
