import re


def convert(num_id: int, table: str) -> int:
    for line in table.splitlines():
        destination_start, source_start, range_length = map(int, line.split())
        source_end = source_start + range_length

        if source_start <= num_id < source_end:
            return destination_start + num_id - source_start

    return num_id


def seeds_to_locations(seeds: list[int], tables_list: list[str]) -> list[int]:
    tables = [table.split(":\n") for table in tables_list]
    locations = []
    for seed in seeds:
        current_number_id = seed
        for table in tables:
            current_number_id = convert(current_number_id, table[1])

        locations.append(current_number_id)

    return locations


def range_of_seeds_to_locations(tables: str) -> list[int]:
    tables_list = tables.split("\n\n")
    seeds_ranges_description = re.findall(r"\d+ \d+", tables_list[0])

    seeds_ranges = [
        [int(i) for i in seed_range_description.split()]
        for seed_range_description in seeds_ranges_description
    ]
    seeds = []
    for start, length in seeds_ranges:
        seeds.extend(range(start, start + length))

    return seeds_to_locations(seeds, tables_list[1:])


if __name__ == "__main__":
    with open("../input.txt", "r") as file:
        input_text = file.read()
        print(
            "The lowest location number for the ranges of seeds is",
            min(range_of_seeds_to_locations(input_text)),
        )
