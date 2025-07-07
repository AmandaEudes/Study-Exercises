from study_exercises.multiples_of_3_or_5 import multiples_of_3_or_5


def test_one() -> None:
    assert 23 == multiples_of_3_or_5(10)


def test_two() -> None:
    assert 0 == multiples_of_3_or_5(-10)


def test_three() -> None:
    assert 233168 == multiples_of_3_or_5(1_000)


def test_four() -> None:
    assert 0 == multiples_of_3_or_5(0)


def test_five() -> None:
    assert 0 == multiples_of_3_or_5(3)


def test_six() -> None:
    assert 3 == multiples_of_3_or_5(4)
