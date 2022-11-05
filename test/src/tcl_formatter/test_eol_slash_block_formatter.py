from src.tcl_formatter.eol_slash_block_formatter import EolSlashBLockFormatter


def test_block_get_longest_line_length_single():
    block = ["\t\tcode \\\n"]
    assert EolSlashBLockFormatter._get_longest_line_length(block) == 15

def test_block_get_longest_line_length(unformatted_block):
    assert EolSlashBLockFormatter._get_longest_line_length(unformatted_block) == 32

def test_block_format(unformatted_block, formatted_block):
    actual_block = EolSlashBLockFormatter.format_block(unformatted_block)
    for actual_line, expected_line in zip(actual_block, formatted_block):
        assert actual_line == expected_line
