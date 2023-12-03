import re


def get_sum_calibration_values(txt_file: str):
    return sum(get_line_calibration_value(line) for line in txt_file.splitlines())


def get_line_calibration_value(line: str):
    def replace_with_digit(match_object: re.Match):
        if match_object.group(0) == "one":
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
        r"one|two|three|four|five|six|seven|eight|nine",
        replace_with_digit,
        line,
    )
    # for index, spelled_out_digit in enumerate(spelled_out_digits, start=1):
    #     line = line.replace(spelled_out_digit, str(index))
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