import re


def get_winning_and_i_have_numbers(
    card: str,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    _, winning_numbers, i_have_numbers = re.split(r"[:|]", card)

    winning_numbers = tuple(
        int(winning_number) for winning_number in winning_numbers.split()
    )
    i_have_numbers = tuple(
        int(i_have_numbers) for i_have_numbers in i_have_numbers.split()
    )

    return winning_numbers, i_have_numbers
