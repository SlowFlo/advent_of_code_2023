import re
from itertools import product


def get_coordinates_to_check(
    multi_lines_str: str,
) -> dict[int, tuple[tuple[int, int], ...]]:
    numbers = re.findall(r"\d+", multi_lines_str)
    lines = multi_lines_str.splitlines()

    coordinates = {}

    def in_range(x, y):
        return 0 <= x < len(lines) and 0 <= y < len(lines[0])

    for number in numbers:
        for line_coord, line in enumerate(lines):
            match = re.search(number, line)
            if match:
                check_coords = [
                    (check_line_coord, check_char_coord)
                    for check_line_coord, check_char_coord in product(
                        range(line_coord - 1, line_coord + 2),
                        range(match.start() - 1, match.end() + 1),
                    )
                    if in_range(check_line_coord, check_char_coord)
                    and (check_line_coord, check_char_coord)
                    not in product([line_coord], range(match.start(), match.end()))
                ]
                coordinates[int(number)] = tuple(check_coords)
                break  # skip remaining lines once the number is found

    return coordinates
