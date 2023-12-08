import re
from itertools import product


def get_check_coords(
    lines: list[str], line_coord: int, match: re.Match
) -> tuple[tuple[int, int], ...]:
    def in_range(x, y):
        return 0 <= x < len(lines) and 0 <= y < len(lines[0])

    return tuple(
        (check_line_coord, check_char_coord)
        for check_line_coord, check_char_coord in product(
            range(line_coord - 1, line_coord + 2),
            range(match.start() - 1, match.end() + 1),
        )
        if in_range(check_line_coord, check_char_coord)
        and (check_line_coord, check_char_coord)
        not in product([line_coord], range(match.start(), match.end()))
    )


def get_coordinates_to_check(
    multi_lines_str: str,
) -> dict[int, tuple[tuple[int, int], ...]]:
    numbers = re.findall(r"\d+", multi_lines_str)
    lines = multi_lines_str.splitlines()

    coordinates = {}

    for number in numbers:
        coordinates[int(number)] = []
        for line_coord, line in enumerate(lines):
            for match in re.finditer(number, line):
                check_coords = get_check_coords(lines, line_coord, match)
                coordinates[int(number)].append(tuple(check_coords))

    return coordinates


def get_part_numbers(multi_lines_str: str) -> list[int]:
    coordinates_to_check = get_coordinates_to_check(multi_lines_str)
    lines = multi_lines_str.splitlines()
    part_numbers = []

    for number, coordinates_lists in coordinates_to_check.items():
        for coordinates in coordinates_lists:
            for line_coord, char_coord in coordinates:
                char = lines[line_coord][char_coord]
                if char != "." and not char.isalnum():
                    part_numbers.append(number)
                    break

    return part_numbers


if __name__ == "__main__":
    with open("../input.txt", "r") as file:
        input_text = file.read()
        print(
            "The sum of all of the part numbers in the engine schematic is:",
            sum(get_part_numbers(input_text)),
        )
