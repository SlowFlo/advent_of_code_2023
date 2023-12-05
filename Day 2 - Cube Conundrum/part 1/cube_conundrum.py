import re
from typing import Dict


def get_game_colors_maximum(game: str) -> Dict[str, int]:
    colors_count = re.split(", |; ", game)

    colors_dict = {"red": 0, "green": 0, "blue": 0}

    for color_count in colors_count:
        count, color = color_count.split()
        count = int(count)
        if colors_dict[color] < count:
            colors_dict[color] = count

    return colors_dict
