from main import marks_matrix

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

print(lower_higher(students_marks))