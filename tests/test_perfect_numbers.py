from pytest import raises
from study_exercises.perfect_numbers import classify_number


def test_one() -> None:
    assert "Perfect" == classify_number(6)


def test_two() -> None:
    assert "Perfect" == classify_number(28)


def test_three() -> None:
    assert "Abundant" == classify_number(12)


def test_four() -> None:
    assert "Abundant" == classify_number(24)


def test_five() -> None:
    assert "Deficient" == classify_number(8)


def test_six() -> None:
    assert "Deficient" == classify_number(2)


def test_seven() -> None:
    assert all("Deficient" == classify_number(value) for value in [8, 2])


def test_eight() -> None:
    assert [6, 28] == [
        value for value in [6, 28, 12, 24, 8, 2] if classify_number(value) == "Perfect"
    ]
