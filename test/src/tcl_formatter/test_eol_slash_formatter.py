from src.tcl_formatter.eol_slash_formatter import EolSlashFormatter

def test_find_blocks_positions(unformatted_code, unformatted_garchomp):
    blocks_positions = EolSlashFormatter.find_blocks_positions(unformatted_code)
    blocks_positions_garchomp = EolSlashFormatter.find_blocks_positions(unformatted_garchomp)
    assert blocks_positions == [[4, 8], [14, 20]]
    assert blocks_positions_garchomp == [[0, 4], [5, 14], [15, 16]]

def test_format_file(unformatted_code, formatted_code):
    actual = EolSlashFormatter.format_block(unformatted_code)
    assert actual == formatted_code

def test_format_file_garchomp(unformatted_garchomp, formatted_garchomp):
    actual = EolSlashFormatter.format_block(unformatted_garchomp)
    assert actual == formatted_garchomp
