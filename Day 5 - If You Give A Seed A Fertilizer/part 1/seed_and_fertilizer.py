def convert(num_id: int, table: str) -> int:
    for line in table.splitlines():
        destination_start, source_start, range_length = map(int, line.split())
        if num_id in range(source_start, source_start + range_length):
            return destination_start + num_id - source_start

    return num_id


def seeds_to_location(tables: str) -> list[int]:
    tables_list = tables.split("\n\n")
    seeds = map(int, tables_list[0].split()[1:])

    _, first_table = tables_list[1].split(":\n")
    locations = []
    for seed in seeds:
        locations.append(convert(seed, first_table))

    return locations
