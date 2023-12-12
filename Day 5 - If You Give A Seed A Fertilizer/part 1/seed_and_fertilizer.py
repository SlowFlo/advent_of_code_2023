def convert(num_id: int, table: str) -> int:
    for line in table.splitlines():
        destination_start, source_start, range_length = map(int, line.split())
        if num_id in range(source_start, source_start + range_length):
            return destination_start + num_id - source_start

    return num_id


def seed_to_location(tables: str) -> int:
    tables_list = tables.split("\n\n")
    seed = int(tables_list[0].split()[1])
    _, first_table = tables_list[1].split(":\n")
    return convert(seed, first_table)
