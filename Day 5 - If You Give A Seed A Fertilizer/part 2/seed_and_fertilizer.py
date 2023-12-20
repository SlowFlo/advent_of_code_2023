import re
from typing import Iterable


class RangeMapper:
    def __init__(self, table_str: str):
        split_lines = table_str.splitlines()
        self.table = [list(map(int, line.split())) for line in split_lines]

    def transform_ranges(self, input_range: range) -> list[range]:
        untreated_ranges = [input_range]
        transformed_ranges = []

        for destination_start, source_start, length in self.table:
            source_end = source_start + length
            newly_untreated_ranges = []

            for untreated_range in untreated_ranges:
                if (
                    source_end <= untreated_range.start
                    or source_start >= untreated_range.stop
                ):
                    newly_untreated_ranges.append(untreated_range)
                    continue

                # Compute the overlapping of the source range with the current untreated range
                overlap_start = max(untreated_range.start, source_start)
                overlap_end = min(untreated_range.stop, source_end)

                # Transform the overlapping range
                offset = destination_start - source_start
                transformed_start = overlap_start + offset
                transformed_length = overlap_end - overlap_start

                transformed_ranges.append(
                    range(transformed_start, transformed_start + transformed_length)
                )

                # Adjust the current untreated range, remove the transformed part
                if untreated_range.start < overlap_start:
                    newly_untreated_ranges.append(
                        range(untreated_range.start, overlap_start)
                    )
                if overlap_end < untreated_range.stop:
                    newly_untreated_ranges.append(
                        range(overlap_end, untreated_range.stop)
                    )

            untreated_ranges = newly_untreated_ranges

        # Append untreated ranges to the result
        transformed_ranges.extend(untreated_ranges)

        return transformed_ranges


def apply_range_transformations(
    tables_list: list[str], seeds_ranges: list[range]
) -> list[range]:
    ranges_mappers = [RangeMapper(table.split(":\n")[1]) for table in tables_list]

    current_ranges = seeds_ranges
    for range_mapper in ranges_mappers:
        new_ranges = []
        for current_range in current_ranges:
            new_ranges.extend(range_mapper.transform_ranges(current_range))
        current_ranges = new_ranges

    return current_ranges


def get_min_location(input_txt: str) -> int:
    tables_list = input_txt.split("\n\n")
    seeds_ranges_description = re.findall(r"\d+ \d+", tables_list[0])

    seeds_ranges = [
        range(int(srd.split()[0]), int(srd.split()[0]) + int(srd.split()[1]))
        for srd in seeds_ranges_description
    ]

    final_ranges = apply_range_transformations(tables_list[1:], seeds_ranges)

    return min([final_range.start for final_range in final_ranges])


if __name__ == "__main__":
    with open("../input.txt", "r") as file:
        input_text = file.read()
        print(
            "The lowest location number for the ranges of seeds is",
            get_min_location(input_text),
        )
