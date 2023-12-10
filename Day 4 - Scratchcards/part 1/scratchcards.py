import re


class Scratchcard:
    def __init__(self, card: str):
        _, winning_numbers, numbers_i_have = re.split(r"[:|]", card)

        self.winning_numbers = set(
            int(winning_number) for winning_number in winning_numbers.split()
        )
        self.numbers_i_have = set(
            int(numbers_i_have) for numbers_i_have in numbers_i_have.split()
        )
        self.winning_numbers_i_have = self.winning_numbers.intersection(
            self.numbers_i_have
        )
