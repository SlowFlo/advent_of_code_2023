from trebuchet import get_line_calibration_value


def test_one_digit_is_found_twice():
    assert get_line_calibration_value("1") == 11
    assert get_line_calibration_value("2") == 22


def test_2_digits_is_the_same():
    assert get_line_calibration_value("23") == 23


def test_3_digits_is_without_the_middle_one():
    assert get_line_calibration_value("456") == 46
    assert get_line_calibration_value("789") == 79


def test_has_letters_between_is_ok():
    assert get_line_calibration_value("1abc2") == 12


def test_has_letters_on_sides_is_ok():
    assert get_line_calibration_value("pqr3stu8vwx") == 38
