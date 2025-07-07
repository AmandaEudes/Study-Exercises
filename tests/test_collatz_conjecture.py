from pytest import raises
from study_exercises.collatz_conjecture import collatz_steps

text_error = "Only positive integers are allowed"


def test_one() -> None:
    assert 9 == collatz_steps(12)


def test_two() -> None:
    assert 0 == collatz_steps(1)


def test_three() -> None:
    with raises(ValueError, match=text_error):
        collatz_steps(-1)


def test_four() -> None:
    with raises(ValueError, match=text_error):
        collatz_steps(12.1)


def test_five() -> None:
    with raises(ValueError, match=text_error):
        collatz_steps(0)


def test_six() -> None:
    assert 152 == collatz_steps(1_000_000)
