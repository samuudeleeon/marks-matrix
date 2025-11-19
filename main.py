# MIT License
#
# Copyright (c) 2025 Daniel López Guimaraes
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def marks_matrix(students_marks: dict[str, int]) -> list[list[int | str]]:
    """
    Builds an ordered list of lists for each score given alongside the students that have obtained such score.

    Args:
        students_marks: dict[str, int]:
            A dictionary whose keys are each students' name with the value being their score.
            Example: {"Sarah": 7, "Leo": 3}

    Returns:
        The matrix containing each scores and the students who have obtained it, ordered from lowest to highest.
        Example: [[3, "Leo"], [7, "Sarah"]]
    """
    groups = {}

    for name, mark in students_marks.items():
        if mark not in groups:
            groups[mark] = []

        groups[mark].append(name)

    matrix = []
    for mark in sorted(groups.keys()):
        students = groups[mark]
        row = [mark] + students
        matrix.append(row)

    return matrix


students_marks = {
    "Alice": 7, "Bob": 9, "Charlie": 3, "Diana": 7, "Ethan": 4,
    "Fiona": 3, "George": 7, "Hannah": 6, "Ian": 5, "Julia": 3,
    "Kevin": 9, "Laura": 7, "Michael": 0, "Nina": 7, "Oliver": 5,
    "Paula": 3, "Quentin": 2, "Rachel": 0, "Samuel": 10, "Tina": 5,
    "Uma": 1, "Victor": 1, "Wendy": 8, "Xavier": 6, "Yvonne": 0,
    "Zachary": 2, "Aaron": 3, "Beth": 10, "Carl": 7, "Deborah": 9,
    "Edward": 6, "Faith": 3, "Gordon": 1, "Helen": 10, "Isaac": 2,
    "Janet": 2, "Kyle": 3, "Lily": 9, "Martin": 6, "Nancy": 2,
    "Oscar": 4, "Patricia": 8, "Ronald": 10, "Sophia": 2, "Thomas": 9,
    "Ursula": 9, "Vera": 8, "William": 0, "Xenia": 1, "Yosef": 1
}

def main():
    """
    The main function of the program.
    """

    # TODO - Show average score
    # TODO - Show most often score
    # TODO - Show least often score
    # TODO - Show highest and lowest score
    marks = marks_matrix(students_marks)
    for mark in marks:
        print(mark)

if __name__ == "__main__":
    main()


def lower_higher(marks: dict[str, int]) -> list[list[int | int]]:
    """
    Builds a list showing the lowest mark alongside the number of students that were given that score.

    Args:
        Takes the same argument as the main function does.
        students_marks: dict[str, int]:
            A dictionary whose keys are each students' name with the value being their score.
            Example: {"Sarah": 7, "Leo": 3}

    Returns:
        The matrix containing the lowest and the highest marks and the times they were given.
        The list containing two tuples, one with the lowest mark and the times it was given, the other one
        with the highest mark and the times it was given.
        Example: [(2, 1), (10, 3)]
    """

    list_lower_higher = []
    matrix = marks_matrix(marks)

    lowest = matrix[0]
    highest = matrix[-1]

    lowest_count = len(lowest) - 1
    highest_count = len(highest) - 1

    list_lower_higher.append((lowest[0], lowest_count))
    list_lower_higher.append((highest[0], highest_count))

    return list_lower_higher
