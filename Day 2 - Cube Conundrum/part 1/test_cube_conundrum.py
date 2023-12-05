from cube_conundrum import get_game_colors_minimum, is_game_possible


def test_get_each_color_maximum():
    assert get_game_colors_minimum(
        "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    ) == {"blue": 6, "red": 4, "green": 2}
    assert get_game_colors_minimum(
        "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    ) == {"blue": 4, "red": 1, "green": 3}
    assert get_game_colors_minimum(
        "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    ) == {"blue": 6, "red": 20, "green": 13}
    assert get_game_colors_minimum(
        "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    ) == {"blue": 15, "red": 14, "green": 3}
    assert get_game_colors_minimum(
        "6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ) == {"blue": 2, "red": 6, "green": 3}


def test_can_tell_if_game_is_possible():
    assert (
        is_game_possible(
            {"red": 12, "green": 13, "blue": 14},
            "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        )
        == True
    )
    assert (
        is_game_possible(
            {"red": 12, "green": 13, "blue": 14},
            "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        )
        == True
    )
    assert (
        is_game_possible(
            {"red": 12, "green": 13, "blue": 14},
            "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        )
        == False
    )
    assert (
        is_game_possible(
            {"red": 12, "green": 13, "blue": 14},
            "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        )
        == False
    )
    assert (
        is_game_possible(
            {"red": 12, "green": 13, "blue": 14},
            "6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        )
        == True
    )
