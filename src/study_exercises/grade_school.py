# Instructions
# Given students' names along with the grade they are in, create a roster for
# the school.

# In the end, you should be able to:

# - Add a student's name to the roster for a grade:
#   - "Add Jim to grade 2."
#   - "OK."

# - Get a list of all students enrolled in a grade:
#   - "Which students are in grade 2?"
#   - "We've only got Jim right now."

# - Get a sorted list of all students in all grades. Grades should be sorted as
# 1, 2, 3, etc., and students within a grade should be sorted alphabetically by
# name.
#   - "Who is enrolled in school right now?"
#   - "Let me think. We have Anna, Barb, and Charlie in grade 1, Alex, Peter,
# and Zoe in grade 2, and Jim in grade 5. So the answer is: Anna, Barb, Charlie,
# Alex, Peter, Zoe, and Jim."

# Note that all our students only have one name (it's a small town, what do you
# want?), and each student cannot be added more than once to a grade or the
# roster. If a test attempts to add the same student more than once, your
# implementation should indicate that this is incorrect.

# The tests for this exercise expect your school roster will be implemented via
# a School class in Python. If you are unfamiliar with classes in Python,
# classes from the Python docs is a good place to start.

# https://exercism.org/tracks/python/exercises/grade-school


class GradeSchool:
    def __init__(self) -> None:
        self.students: dict[int, list[str]] = {}
        self.added_log: list[bool] = []

    def __repr__(self) -> str:
        """Return string representation of the GradeSchool object.

        Returns:
            str: String showing the grades dictionary content
        """
        return f"GradeSchool(grades={self.students})"

    def AddStudent(self, name: str, grade: int) -> None:
        self.students.setdefault(grade, [])

        if name in set(self.Roster()):
            self.added_log.append(False)
        else:
            self.students[grade].append(name)
            self.added_log.append(True)

    def Added(self) -> list[bool]:
        counter = self.added_log
        self.added_log = []
        return counter

    def Roster(self) -> list[str]:
        return [
            name
            for grade in sorted(self.students.keys())
            for name in sorted(self.students[grade])
        ]

    def Grade(self, grade_number: int) -> list[str]:
        return sorted(self.students.get(grade_number, []))
