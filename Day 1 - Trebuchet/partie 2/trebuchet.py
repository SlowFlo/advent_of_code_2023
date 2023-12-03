import re


def get_sum_calibration_values(txt_file: str):
    return sum(get_line_calibration_value(line) for line in txt_file.splitlines())


def get_line_calibration_value(line: str):
    def replace_with_digit(match_object: re.Match):
        if match_object.group(0) == "oneight":
            return "18"
        elif match_object.group(0) == "twone":
            return "21"
        elif match_object.group(0) == "threeight":
            return "38"
        elif match_object.group(0) == "fiveight":
            return "58"
        elif match_object.group(0) == "sevenine":
            return "79"
        elif match_object.group(0) == "eightwo":
            return "82"
        elif match_object.group(0) == "eighthree":
            return "83"
        elif match_object.group(0) == "nineight":
            return "98"
        elif match_object.group(0) == "one":
            return "1"
        elif match_object.group(0) == "two":
            return "2"
        elif match_object.group(0) == "three":
            return "3"
        elif match_object.group(0) == "four":
            return "4"
        elif match_object.group(0) == "five":
            return "5"
        elif match_object.group(0) == "six":
            return "6"
        elif match_object.group(0) == "seven":
            return "7"
        elif match_object.group(0) == "eight":
            return "8"
        elif match_object.group(0) == "nine":
            return "9"

    line = re.sub(
        r"oneight|twone|threeight|fiveight|sevenine|eightwo|eighthree|nineight|one|two|three|four|five|six|seven|eight|nine",
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
            "The sum of all calibration values are:",
            get_sum_calibration_values(input_text),
        )
