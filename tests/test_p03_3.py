from exercises.p03_3 import homework_03


def test_homework_03_returns_square_dictionary():
    assert homework_03(3) == {1: 1, 2: 4, 3: 9}


def test_homework_03_returns_error_for_non_integer_input():
    assert homework_03(8.5) == {"error": "Vui lòng nhập một số nguyên."}
