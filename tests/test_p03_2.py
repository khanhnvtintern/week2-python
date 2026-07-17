from exercises.p03_2 import homework_02

def test_homework_02_returns():
    assert homework_02(8) ==  40320


def test_homework_02_returns_error_for_non_integer_input():
    assert homework_02(8.5) == {"error": "Vui lòng nhập một số nguyên."}