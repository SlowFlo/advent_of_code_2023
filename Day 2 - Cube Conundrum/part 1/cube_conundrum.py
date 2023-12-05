import re
from typing import Dict


def get_game_colors_minimum(game: str) -> Dict[str, int]:
    colors_count = re.split(", |; ", game)

    colors_dict = {"red": 0, "green": 0, "blue": 0}

    for color_count in colors_count:
        count, color = color_count.split()
        count = int(count)
        if colors_dict[color] < count:
            colors_dict[color] = count

    return colors_dict


def is_game_possible(bag_content: Dict[str, int], game: str) -> bool:
    colors_min_detected = get_game_colors_minimum(game)

    game_is_possible = True
    for color in bag_content:
        if colors_min_detected[color] > bag_content[color]:
            game_is_possible = False

    return game_is_possible


def get_sum_of_possible_games_ids(bag_content: Dict[str, int], txt_file: str) -> int:
    sum_of_possible_games_ids = 0

    for line in txt_file.splitlines():
        game_id, game = line.split(": ")
        if is_game_possible(bag_content, game):
            game_id = int(game_id.split()[1])  # ex: "Game 1"
            sum_of_possible_games_ids += game_id

    return sum_of_possible_games_ids


if __name__ == "__main__":
    with open("../input.txt", "r") as file:
        input_text = file.read()
        print(
            "The sum of all possible games IDs is:",
            get_sum_of_possible_games_ids(
                {"red": 12, "green": 13, "blue": 14}, input_text
            ),
        )
