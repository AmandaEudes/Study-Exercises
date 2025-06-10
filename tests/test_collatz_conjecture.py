from study_exercises.collatz_conjecture import collatz_steps


def test_one() -> None:
    assert 9 == collatz_steps(12)


def test_two() -> None:
    assert 0 == collatz_steps(1)
