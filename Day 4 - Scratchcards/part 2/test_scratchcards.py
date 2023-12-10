from scratchcards import Scratchcard, PileOfScratchcards


def test_get_winning_and_i_have_numbers():
    card = Scratchcard("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert card.winning_numbers == {41, 48, 83, 86, 17}
    assert card.numbers_i_have == {83, 86, 6, 31, 17, 9, 48, 53}


def test_get_winning_numbers_i_have():
    card = Scratchcard("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert card.winning_numbers_i_have == {48, 83, 17, 86}

    card = Scratchcard("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")
    assert card.winning_numbers_i_have == set()


def test_get_points():
    card = Scratchcard("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert card.get_points() == 8

    card = Scratchcard("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19")
    assert card.get_points() == 2

    card = Scratchcard("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1")
    assert card.get_points() == 2

    card = Scratchcard("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83")
    assert card.get_points() == 1

    card = Scratchcard("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")
    assert card.get_points() == 0

    card = Scratchcard("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")
    assert card.get_points() == 0


def test_get_total_points():
    multi_lines_str = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    pile = PileOfScratchcards(multi_lines_str)
    assert pile.get_total_points() == 13


def test_get_copied_cards_id():
    card = Scratchcard("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert card.get_copies_id() == (2, 3, 4, 5)


def test_get_number_of_copies():
    multi_lines_str = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    pile = PileOfScratchcards(multi_lines_str)
    assert pile.get_number_of_copies() == {1: 1, 2: 2, 3: 4, 4: 8, 5: 14, 6: 1}
