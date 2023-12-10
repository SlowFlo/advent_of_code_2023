from scratchcards import Scratchcard


def test_get_winning_and_i_have_numbers():
    card = Scratchcard("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert card.winning_numbers == (41, 48, 83, 86, 17)
    assert card.numbers_i_have == (83, 86, 6, 31, 17, 9, 48, 53)
