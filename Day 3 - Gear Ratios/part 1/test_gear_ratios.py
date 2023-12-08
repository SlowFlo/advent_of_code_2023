from gear_ratios import get_coordinates_to_check, get_part_numbers


def test_detect_coordinates_to_check():
    multi_lines_str = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    coordinates = {
        35: [
            (
                (1, 1),
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 1),
                (2, 4),
                (3, 1),
                (3, 2),
                (3, 3),
                (3, 4),
            )
        ],
        58: [
            (
                (4, 6),
                (4, 7),
                (4, 8),
                (4, 9),
                (5, 6),
                (5, 9),
                (6, 6),
                (6, 7),
                (6, 8),
                (6, 9),
            )
        ],
        114: [((0, 4), (0, 8), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8))],
        467: [((0, 3), (1, 0), (1, 1), (1, 2), (1, 3))],
        592: [
            (
                (5, 1),
                (5, 2),
                (5, 3),
                (5, 4),
                (5, 5),
                (6, 1),
                (6, 5),
                (7, 1),
                (7, 2),
                (7, 3),
                (7, 4),
                (7, 5),
            )
        ],
        598: [((8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (9, 4), (9, 8))],
        617: [((3, 0), (3, 1), (3, 2), (3, 3), (4, 3), (5, 0), (5, 1), (5, 2), (5, 3))],
        633: [
            (
                (1, 5),
                (1, 6),
                (1, 7),
                (1, 8),
                (1, 9),
                (2, 5),
                (2, 9),
                (3, 5),
                (3, 6),
                (3, 7),
                (3, 8),
                (3, 9),
            )
        ],
        664: [((8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (9, 0), (9, 4))],
        755: [
            (
                (6, 5),
                (6, 6),
                (6, 7),
                (6, 8),
                (6, 9),
                (7, 5),
                (7, 9),
                (8, 5),
                (8, 6),
                (8, 7),
                (8, 8),
                (8, 9),
            )
        ],
    }

    assert get_coordinates_to_check(multi_lines_str) == coordinates


def test_detect_coordinates_to_check_when_duplicate_numbers():
    multi_lines_str = """
467..114..
...*......
..35..633.
......#...
467*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    coordinates = {
        35: [
            (
                (1, 1),
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 1),
                (2, 4),
                (3, 1),
                (3, 2),
                (3, 3),
                (3, 4),
            )
        ],
        58: [
            (
                (4, 6),
                (4, 7),
                (4, 8),
                (4, 9),
                (5, 6),
                (5, 9),
                (6, 6),
                (6, 7),
                (6, 8),
                (6, 9),
            )
        ],
        114: [((0, 4), (0, 8), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8))],
        467: [
            ((0, 3), (1, 0), (1, 1), (1, 2), (1, 3)),
            ((3, 0), (3, 1), (3, 2), (3, 3), (4, 3), (5, 0), (5, 1), (5, 2), (5, 3)),
        ],
        592: [
            (
                (5, 1),
                (5, 2),
                (5, 3),
                (5, 4),
                (5, 5),
                (6, 1),
                (6, 5),
                (7, 1),
                (7, 2),
                (7, 3),
                (7, 4),
                (7, 5),
            )
        ],
        598: [((8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (9, 4), (9, 8))],
        633: [
            (
                (1, 5),
                (1, 6),
                (1, 7),
                (1, 8),
                (1, 9),
                (2, 5),
                (2, 9),
                (3, 5),
                (3, 6),
                (3, 7),
                (3, 8),
                (3, 9),
            )
        ],
        664: [((8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (9, 0), (9, 4))],
        755: [
            (
                (6, 5),
                (6, 6),
                (6, 7),
                (6, 8),
                (6, 9),
                (7, 5),
                (7, 9),
                (8, 5),
                (8, 6),
                (8, 7),
                (8, 8),
                (8, 9),
            )
        ],
    }

    assert get_coordinates_to_check(multi_lines_str) == coordinates


def test_get_part_numbers():
    multi_lines_str = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    assert get_part_numbers(multi_lines_str) == [467, 35, 633, 617, 592, 755, 664, 598]


def test_get_part_numbers_when_2_numbers_for_1_symbol():
    multi_lines_str = """12
#3"""

    assert get_part_numbers(multi_lines_str) == [12, 3]

    multi_lines_str = """12.34
..#.."""

    assert get_part_numbers(multi_lines_str) == [12, 34]


def test_get_part_numbers_when_1_number_for_2_symbols():
    multi_lines_str = """#12#"""

    assert get_part_numbers(multi_lines_str) == [12]


def test_get_part_numbers_when_no_ok_part_in_string():
    multi_lines_str = """8....#"""

    assert get_part_numbers(multi_lines_str) == []


def test_get_part_numbers_when_4_numbers_on_diagonals_for_1_symbol():
    multi_lines_str = """2.2
.*.
1.1"""

    assert get_part_numbers(multi_lines_str) == [2, 2, 1, 1]


def test_advanced_test_case():
    multi_lines_str = """12.......*..
+.........34
.......-12..
..78........
..*....60...
78..........
.......23...
....90*12...
............
2.2......12.
.*.........*
1.1.......56"""

    assert sum(get_part_numbers(multi_lines_str)) == 413
