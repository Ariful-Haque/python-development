#!/usr/local/bin/python3.7

age = 34

print("my age is " + str(age) + " years")

# replacement field

print("my age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, and {4}."\
        .format("30", "April", "June", "September", "November"))

print("""
         January: {2}
         February: {0}
         March: {2}
         April: {1}
         May: {2}
         June: {1}
         July: {2}
         August: {2}
         September: {1}
         October: {2}
         November: {1}
         December: {2}
         """.format(28, 30, 31))

# string formatting operator
# deprecated

print("My age is %d years" % age)
print("My age is %d %s and %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No %2d squared is %4d and cubed is %4d" % (i, i**2, i**3))

print("Pi is approximately %.50f" % (22 / 7))

# doing the same calculation with replacement field syntax
# number after : represents number of spaces
# and < represents output is left justified.
for i in range(1, 12):
    print("No {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))

print("Pi is approximately {0:.50f}".format(22 / 7))



