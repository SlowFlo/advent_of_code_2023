from scratchcards import Scratchcard


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
