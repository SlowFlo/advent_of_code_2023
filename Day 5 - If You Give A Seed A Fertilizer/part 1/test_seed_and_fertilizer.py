def test_convert_when_not_in_range():
    table = """50 98 2
52 50 48"""

    assert convert(1, table) == 1
