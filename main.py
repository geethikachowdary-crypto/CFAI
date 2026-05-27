# =====================================================
# AI Examination Seating Arrangement System
# =====================================================

class Student:

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept


students = [
    Student("Ravi", "CSE"),
    Student("Priya", "ECE"),
    Student("Arjun", "CSE"),
    Student("Sneha", "IT")
]


seats = ["A1", "A2", "B1", "B2"]

seat_allocation = {}

adjacent = {
    "A1": ["A2", "B1"],
    "A2": ["A1", "B2"],
    "B1": ["A1", "B2"],
    "B2": ["A2", "B1"]
}


# =====================================================
# Constraint Checking
# =====================================================


def valid(student, seat):

    for adj in adjacent[seat]:

        if adj in seat_allocation:

            other_student = seat_allocation[adj]

            if other_student.dept == student.dept:
                return False

    return True


# =====================================================
# Utility Evaluation
# =====================================================


def utility():

    conflicts = 0

    for seat in seat_allocation:

        for adj in adjacent[seat]:

            if adj in seat_allocation:

                if seat_allocation[seat].dept == seat_allocation[adj].dept:
                    conflicts += 1

    return 100 - conflicts


# =====================================================
# Backtracking Search
# =====================================================


def allocate(index):

    if index == len(students):
        return True

    student = students[index]

    for seat in seats:

        if seat not in seat_allocation:

            if valid(student, seat):

                seat_allocation[seat] = student

                print("Allocated", student.name, "to", seat)

                if allocate(index + 1):
                    return True

                print("Backtracking from", seat)

                del seat_allocation[seat]

    return False


# =====================================================
# Main Program
# =====================================================

print("\nAI Examination Seating Arrangement System\n")

result = allocate(0)

if result:

    print("\nFinal Seating Arrangement:\n")

    for seat in seat_allocation:

        student = seat_allocation[seat]

        print(seat, "->", student.name, "(", student.dept, ")")

    print("\nUtility Score:", utility())

    probability_safe = 0.85

    print("Probability of Safe Seating:", probability_safe)

else:

    print("No valid arrangement found")
    print("Reason: constraints could not be satisfied")