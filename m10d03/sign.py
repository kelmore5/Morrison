def sgn(num):
    # returns -1 for negative numbers, 1 for positive, 0 for 0.
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0

x = -5
print("sgn(%s) = %s, expected: %s)" % (x, sgn(x), -1))
x = 0
print("sgn(%s) = %s, expected: %s)" % (x, sgn(x), 0))
x = 5
print("sgn(%s) = %s, expected: %s)" % (x, sgn(x), 1))

