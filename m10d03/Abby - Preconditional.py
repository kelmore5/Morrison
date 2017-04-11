def abs1(x):  # to define f(x), Boss statement (owns indented code)
    """prec: x is an integer
postc: returns x if x is positive, -x if x is negative"""
    return x if x >= 0 else -x


def abs2(x):
    """prec: x is an integer
postc: returns x if x is positive, -x if x is negative"""
    if x < 0:  # if x < 0
        x = -x  # x gets -x, worker statement, complete sentence
    return x


y = -5
print("The absolute value of %s is %s, expected: %s" % (y, abs1(y), 5))
y = 5
print("The absolute value of %s is %s, expected: %s" % (y, abs1(y), 5))
y = 0
print("The absolute value of %s is %s, expected: %s" % (y, abs1(y), 0))

y = -5
print("The absolute value of %s is %s, expected: %s" % (y, abs2(y), 5))
y = 5
print("The absolute value of %s is %s, expected: %s" % (y, abs2(y), 5))
y = 0
print("The absolute value of %s is %s, expected: %s" % (y, abs2(y), 0))
