from scratchcards import get_winning_and_i_have_numbers


def test_get_winning_and_i_have_numbers():
    card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    assert get_winning_and_i_have_numbers(card) == (
        (41, 48, 83, 86, 17),
        (83, 86, 6, 31, 17, 9, 48, 53),
    )
