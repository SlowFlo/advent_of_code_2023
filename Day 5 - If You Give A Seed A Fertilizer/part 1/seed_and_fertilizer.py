def convert(num_id: int, table: str) -> int:
    for line in table.splitlines():
        destination_start, source_start, range_length = map(int, line.split())
        if num_id in range(source_start, source_start + range_length):
            return destination_start + num_id - source_start

    return num_id
