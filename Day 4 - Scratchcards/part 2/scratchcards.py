import re


class Scratchcard:
    def __init__(self, card: str):
        card_id, winning_numbers, numbers_i_have = re.split(r"[:|]", card)

        self.id = int(card_id.split()[1])
        self.winning_numbers = set(
            winning_number for winning_number in winning_numbers.split()
        )
        self.numbers_i_have = set(
            numbers_i_have for numbers_i_have in numbers_i_have.split()
        )
        self.winning_numbers_i_have = self.winning_numbers.intersection(
            self.numbers_i_have
        )

    def get_points(self) -> int:
        if not self.winning_numbers_i_have:
            return 0

        return 2 ** (len(self.winning_numbers_i_have) - 1)

    def get_copies_id(self) -> tuple[int, ...]:
        return tuple(
            self.id + index + 1 for index, _ in enumerate(self.winning_numbers_i_have)
        )


class PileOfScratchcards:
    def __init__(self, multi_lines_str: str):
        self.cards = [Scratchcard(line) for line in multi_lines_str.splitlines()]

    def get_total_points(self) -> int:
        total_points = 0

        for card in self.cards:
            total_points += card.get_points()

        return total_points

    def get_number_of_copies(self) -> dict[int, int]:
        number_of_copies = {card.id: 1 for card in self.cards}

        for card in self.cards:
            for _ in range(number_of_copies[card.id]):
                for copy_id in card.get_copies_id():
                    number_of_copies[copy_id] += 1

        return number_of_copies


if __name__ == "__main__":
    with open("../input.txt", "r") as file:
        input_text = file.read()
        print(
            "The pile of scratchcards is worth",
            PileOfScratchcards(input_text).get_total_points(),
            "in total.",
        )
        print(
            "At the end I have",
            sum(PileOfScratchcards(input_text).get_number_of_copies().values()),
            "cards.",
        )
