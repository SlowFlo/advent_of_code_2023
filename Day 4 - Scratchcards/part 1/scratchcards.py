import re


class Scratchcard:
    def __init__(self, card: str):
        _, winning_numbers, numbers_i_have = re.split(r"[:|]", card)

        self.winning_numbers = tuple(
            int(winning_number) for winning_number in winning_numbers.split()
        )
        self.numbers_i_have = tuple(
            int(numbers_i_have) for numbers_i_have in numbers_i_have.split()
        )
