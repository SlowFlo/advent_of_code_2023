from seed_and_fertilizer import convert, seeds_to_locations, range_of_seeds_to_locations


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
    tables_list = [
        """seed-to-soil map:
50 98 2
52 50 48"""
    ]

    assert seeds_to_locations([79], tables_list) == [81]


def test_convert_several_seeds_through_one_map():
    tables_list = [
        """seed-to-soil map:
50 98 2
52 50 48""",
    ]

    assert seeds_to_locations([79, 14, 55, 13], tables_list) == [81, 14, 57, 13]


def test_convert_several_seeds_through_several_maps():
    tables_list = [
        """seed-to-soil map:
50 98 2
52 50 48""",
        """soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15""",
        """fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4""",
        """water-to-light map:
88 18 7
18 25 70""",
        """light-to-temperature map:
45 77 23
81 45 19
68 64 13""",
        """temperature-to-humidity map:
0 69 1
1 0 69""",
        """humidity-to-location map:
60 56 37
56 93 4""",
    ]

    assert seeds_to_locations([79, 14, 55, 13], tables_list) == [82, 43, 86, 35]


def test_1_range_through_1_map():
    input_file = """seeds: 79 14

seed-to-soil map:
50 98 2
52 50 48"""

    assert range_of_seeds_to_locations(input_file) == [
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        91,
        92,
        93,
        94,
    ]


def test_2_ranges_through_several_maps():
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

    assert range_of_seeds_to_locations(input_file) == [
        82,
        83,
        84,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        60,
        86,
        87,
        88,
        89,
        94,
        95,
        96,
        56,
        57,
        58,
        59,
        97,
        98,
    ]
