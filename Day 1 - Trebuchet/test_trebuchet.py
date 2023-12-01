from trebuchet import get_line_calibration_value, get_sum_calibration_values


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


def test_advanced_examples_are_ok():
    assert get_line_calibration_value("a1b2c3d4e5f") == 15
    assert get_line_calibration_value("treb7uchet") == 77


def test_sum_of_multi_line_file_is_ok():
    txt_file = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    assert get_sum_calibration_values(txt_file) == 142
