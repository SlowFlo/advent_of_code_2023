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


def test_detect_digits_written_with_letters():
    assert get_line_calibration_value("two1nine") == 29


def test_two_merged_spelled_out_digits_only_first_one_is_ok():
    assert get_line_calibration_value("eightwothree") == 83


def test_more_advanced_examples_are_ok():
    assert get_line_calibration_value("abcone2threexyz") == 13
    assert get_line_calibration_value("xtwone3four") == 24
    assert get_line_calibration_value("4nineeightseven2") == 42
    assert get_line_calibration_value("zoneight234") == 14
    assert get_line_calibration_value("7pqrstsixteen") == 76
