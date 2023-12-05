def get_sum_calibration_values(txt_file: str):
    return sum(get_line_calibration_value(line) for line in txt_file.splitlines())


def get_line_calibration_value(line: str):
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
