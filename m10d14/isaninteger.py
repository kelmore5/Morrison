def isAnInteger(word):
    word = word.strip()
    k = 0
    if word[k] in "+-":
        k += 1
    elif not word[k].isdigit():
        return False
    while k < len(word):
        if not word[k].isdigit():
            return False
    return True

s = "dog"
print(isAnInteger(s))

s = "457"
print(isAnInteger(s))
