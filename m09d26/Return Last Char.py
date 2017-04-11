def last_char(xy):
    """prec: x is a string
postc: returns the last character of the string."""
    return xy[-1]           # method stub or function stub


def last_non_whitespace_char(xy):
    """prec: x is a string
postc: returns the last non-whitespace character"""
    y = xy.rstrip()
    return y[-1]           # method stub or function stub
    
if __name__ == "__main__":
    print("*************Test for lastChar***************")
    a = "cat"
    print("The last character of \"%s\" is %s, expected: %s" % (a, last_char(a), "t"))
    a = "abc123"
    print("The last character of \"%s\" is %s, expected: %s" % (a, last_char(a), "3"))

    print("************Test for lastNonWhitespaceChar**********")
    x = "the dog     "
    print("The last non-whitespace character of \"%s\" is %s, expected: %s" % (x, last_non_whitespace_char(x), "g"))
    x = "1234"
    print("The last non-whitespace character of \"%s\" is %s, expected: %s" % (x, last_non_whitespace_char(x), "4"))
    x = "     pizzA"
    print("The last non-whitespace character of \"%s\" is %s, expected: %s" % (x, last_non_whitespace_char(x), "A"))
