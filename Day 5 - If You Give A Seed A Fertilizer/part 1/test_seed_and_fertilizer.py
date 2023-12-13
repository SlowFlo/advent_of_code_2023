from seed_and_fertilizer import convert, seeds_to_location


def test_convert_when_not_in_range():
    table = """50 98 2
52 50 48"""

    assert convert(0, table) == 0
    assert convert(1, table) == 1
    assert convert(30, table) == 30


def test_convert_when_in_range():
    table = """50 98 2
52 50 48"""

    assert convert(98, table) == 50
    assert convert(99, table) == 51
    assert convert(61, table) == 63


def test_convert_one_seed_through_one_map():
    input_file = """seeds: 79

seed-to-soil map:
50 98 2
52 50 48"""

    assert seeds_to_location(input_file) == [81]


def test_convert_several_seeds_through_one_map():
    input_file = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48"""

    assert seeds_to_location(input_file) == [81, 14, 57, 13]


def test_convert_several_seeds_through_several_maps():
    input_file = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

    assert seeds_to_location(input_file) == [82, 43, 86, 35]
