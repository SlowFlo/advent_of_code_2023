def test_get_each_color_maximum():
    assert get_game_colors_maximum(
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    ) == {"blue": 6, "red": 4, "green": 2}
