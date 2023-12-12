from seed_and_fertilizer import convert


def test_convert_when_not_in_range():
    table = """50 98 2
52 50 48"""

    assert convert(1, table) == 1
    assert convert(30, table) == 30


def test_convert_when_in_range():
    table = """50 98 2
52 50 48"""

    assert convert(98, table) == 50
    assert convert(61, table) == 63
