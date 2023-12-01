from trebuchet import get_line_calibration_value


def test_one_digit_is_found_twice():
    assert get_line_calibration_value("1") == 11
