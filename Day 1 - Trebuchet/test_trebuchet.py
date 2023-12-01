from trebuchet import get_line_calibration_value


def test_one_digit_is_found_twice():
    assert get_line_calibration_value("1") == 11


def test_2_digits_is_the_same():
    assert get_line_calibration_value("23") == 23


def test_3_digits_is_without_the_middle_one():
    assert get_line_calibration_value("456") == 46
