import re


def get_sum_calibration_values(txt_file: str):
    return sum(get_line_calibration_value(line) for line in txt_file.splitlines())


def get_line_calibration_value(line: str):
    def replace_with_digit(match_object: re.Match):
        # keeping one letter on each side for twone => 21 cases
        if match_object.group(0) == "one":
            return "o1e"
        elif match_object.group(0) == "two":
            return "t2o"
        elif match_object.group(0) == "three":
            return "t3e"
        elif match_object.group(0) == "four":
            return "f4r"
        elif match_object.group(0) == "five":
            return "f5e"
        elif match_object.group(0) == "six":
            return "s6x"
        elif match_object.group(0) == "seven":
            return "s7n"
        elif match_object.group(0) == "eight":
            return "e8t"
        elif match_object.group(0) == "nine":
            return "n9e"

    line = re.sub(
        r"one|two|three|four|five|six|seven|eight|nine",
        replace_with_digit,
        line,
    )
    # doing once more for the few remaining cases
    line = re.sub(
        r"one|two|three|four|five|six|seven|eight|nine",
        replace_with_digit,
        line,
    )

    line = "".join(filter(str.isdigit, line))
    if len(line) == 1:
        return int(line + line)
    else:
        return int(line[0] + line[-1])


if __name__ == "__main__":
    with open("../input.txt", "r") as file:
        input_text = file.read()
        print(
            "The sum of all calibration values is:",
            get_sum_calibration_values(input_text),
        )
