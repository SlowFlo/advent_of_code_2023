def convert(num_id: int, table: str) -> int:
    for line in table.splitlines():
        destination_start, source_start, range_length = map(int, line.split())
        if num_id in range(source_start, source_start + range_length):
            return destination_start + num_id - source_start

    return num_id


def seeds_to_locations(tables: str) -> list[int]:
    tables_list = tables.split("\n\n")
    seeds = map(int, tables_list[0].split()[1:])

    tables_iterator = list(map(lambda x: x.split(":\n"), tables_list[1:]))
    locations = []
    for seed in seeds:
        current_number_id = seed
        for table in tables_iterator:
            current_number_id = convert(current_number_id, table[1])

        locations.append(current_number_id)

    return locations


if __name__ == "__main__":
    with open("../input.txt", "r") as file:
        input_text = file.read()
        print("The lowest location number is", min(seeds_to_locations(input_text)))
