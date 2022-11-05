from format_my_code import parse_user_specified_ranges

def test_parse_user_specified_ranges():
    input_range_1 = "5-10"
    input_range_2 = "20-30,40-50"

    expected_range_1 = [[4, 10]]
    expected_range_2 = [[19, 30], [39, 50]]

    actual_range_1 = parse_user_specified_ranges(input_range_1)
    actual_range_2 = parse_user_specified_ranges(input_range_2)

    assert actual_range_1 == expected_range_1
    assert actual_range_2 == expected_range_2
