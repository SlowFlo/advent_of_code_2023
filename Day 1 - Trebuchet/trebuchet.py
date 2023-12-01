def get_line_calibration_value(line: str):
    if len(line) == 1:
        return int(line + line)
    elif len(line) == 2:
        return int(line)
    else:
        return int(line[0] + line[-1])
