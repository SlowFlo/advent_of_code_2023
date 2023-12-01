def get_line_calibration_value(line: str):
    if len(line) == 1:
        return 11
    elif len(line) == 2:
        return 23
    else:
        return 46
