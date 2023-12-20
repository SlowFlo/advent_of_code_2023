from seed_and_fertilizer import (
    RangeMapper,
    apply_range_transformations,
    get_min_location,
)


def test_mapper_transform_when_starting_range_in_table_ranges():
    table = """50 98 2
52 50 48"""

    mapper = RangeMapper(table)

    assert mapper.transform_ranges(range(79, 93)) == [range(81, 95)]
    assert mapper.transform_ranges(range(55, 68)) == [range(57, 70)]


def test_mapper_transform_when_starting_range_not_mapped():
    table = """0 15 37
37 52 2
39 0 15"""

    mapper = RangeMapper(table)

    assert mapper.transform_ranges(range(81, 95)) == [range(81, 95)]
    assert mapper.transform_ranges(range(57, 70)) == [range(57, 70)]


def test_mapper_transform_when_only_a_part_of_starting_range_mapped():
    table = """49 53 8
0 11 42
42 0 7
57 7 4"""

    mapper = RangeMapper(table)

    assert mapper.transform_ranges(range(81, 95)) == [range(81, 95)]
    assert mapper.transform_ranges(range(57, 70)) == [range(53, 57), range(61, 70)]


def test_proceed_seeds_ranges_on_3_successive_tables():
    tables = [
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
    ]

    assert apply_range_transformations(tables, [range(79, 93), range(55, 68)]) == [
        range(81, 95),
        range(53, 57),
        range(61, 70),
    ]


def test_get_min_location_on_example():
    input_txt = """seeds: 79 14 55 13

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

    assert get_min_location(input_txt) == 46
