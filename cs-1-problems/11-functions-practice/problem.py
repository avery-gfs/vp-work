def test(result, expected):
    if result != expected:
        print("!!!!! FAIL !!!!!\n")

    else:
        print("----- PASS -----\n")

    print(result)
    print()


# ----------------------------------------------------------

# Write cToF(c), which converts a temperature in Celsius to Fahrenheit.


def cToF():
    pass


test(cToF(25), 77)
test(cToF(0), 32)
test(cToF(100), 212)

# ----------------------------------------------------------

# Write clamp(n, low, hi), which returns n if it is between low and hi,
# low if n is too small, and hi if n is too big. Assume low <= hi.


def clamp():
    pass


test(clamp(5, 0, 10), 5)
test(clamp(-1, 0, 10), 0)
test(clamp(11, 0, 10), 10)

# ----------------------------------------------------------

# Write letterGrade(points), which returns "A" for 90 and up, "B" for
# 80-89, "C" for 70-79, "D" for 60-69, and "F" for anything lower.


def letterGrade():
    pass


test(letterGrade(99), "A")
test(letterGrade(88), "B")
test(letterGrade(77), "C")
test(letterGrade(66), "D")
test(letterGrade(55), "F")

# ----------------------------------------------------------

# Write product(numbers), which returns all the numbers multiplied together.
# Assume numbers is not empty.


def product():
    pass


test(product([1, 2, 3, 4]), 24)
test(product([4, 5, 6, 0]), 0)

# ----------------------------------------------------------

# Write countEven(numbers), which returns how many of the numbers are even.


def countEven():
    pass


test(countEven([]), 0)
test(countEven([1, 2, 3, 4, -2, 0]), 4)
