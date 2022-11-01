from tcl_formatters.source.block import Block

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
