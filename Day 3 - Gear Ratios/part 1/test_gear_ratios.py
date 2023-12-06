from gear_ratios import get_coordinates


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
        467: ((0, 3), (1, 0), (1, 1), (1, 2), (1, 3)),
        114: ((0, 4), (0, 8), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)),
        35: (
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
        ),
        633: (
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
        ),
        617: ((3, 0), (3, 1), (3, 2), (3, 3), (4, 3), (5, 0), (5, 1), (5, 2), (5, 3)),
        58: (
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
        ),
        592: (
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
        ),
        755: (
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
        ),
        664: ((8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (9, 0), (9, 4)),
        598: ((8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (9, 4), (9, 8)),
    }

    assert get_coordinates(multi_lines_str) == coordinates
