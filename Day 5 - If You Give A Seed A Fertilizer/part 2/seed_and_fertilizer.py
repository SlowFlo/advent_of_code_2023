import re


def convert(num_id: int, table: str) -> int:
    for line in table.splitlines():
        destination_start, source_start, range_length = map(int, line.split())
        if num_id in range(source_start, source_start + range_length):
            return destination_start + num_id - source_start

    return num_id


def seeds_to_locations(seeds: list[int], tables_list: list[str]) -> list[int]:
    tables_iterator = list(map(lambda x: x.split(":\n"), tables_list))
    locations = []
    for seed in seeds:
        current_number_id = seed
        for table in tables_iterator:
            current_number_id = convert(current_number_id, table[1])

        locations.append(current_number_id)

    return locations


def range_of_seeds_to_locations(tables: str) -> list[int]:
    tables_list = tables.split("\n\n")
    seeds_ranges_description = re.findall(r"\d+ \d+", tables_list[0])

    seeds_ranges = [
        list(map(int, seed_range_description.split()))
        for seed_range_description in seeds_ranges_description
    ]
    seeds = []
    for seed_range in seeds_ranges:
        seeds += list(range(seed_range[0], seed_range[0] + seed_range[1]))

    return seeds_to_locations(seeds, tables_list[1:])


if __name__ == "__main__":
    with open("../input.txt", "r") as file:
        input_text = file.read()
        print(
            "The lowest location number for the ranges of seeds is",
            min(range_of_seeds_to_locations(input_text)),
        )
