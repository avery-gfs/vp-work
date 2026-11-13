# Generate a sparkline chart for a list of numbers. Each number is shown as
# one of the bar characters below. The largest number in the list gets the
# tallest bar, and the other numbers get bars scaled to fit, with 0 as the
# bottom of the scale (0 gets the shortest bar). Assume the numbers are all
# positive or zero, and aren't all 0.
#
# See https://en.wikipedia.org/wiki/Sparkline
#
# For the numbers [1, 5, 22, 13, 5, 2, 8, 3, 15, 20] the output should be:
#
# ▁▃█▅▃▂▄▂▆▇
#
# For the numbers [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] the output should be:
#
# ▃▂▄▂▅█▃▆▅▃▅
#
# Hint: look up the built-in max function.

bars = "▁▂▃▄▅▆▇█"

numbers = [1, 5, 22, 13, 5, 2, 8, 3, 15, 20]

chart = ""

# Your code goes here

print(chart)
