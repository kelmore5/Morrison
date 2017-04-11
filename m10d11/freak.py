def mungeChars(word):
    out = {}
    for k in word:
        if k in out.keys():
            out[k] += 1
        else:
            out[k] = 1
    return out


def mungeLetter(word):
    out = {}
    word = word.lower()
    for k in word:
        if k.isalpha():
            if k in out.keys():
                out[k] += 1
            else:
                out[k] = 1
    return out


def makeTable(d):
    print("table")
    for k in d.keys():
        print("<tr><td>%s</td><td>%s</td></tr>" % (k, d[k]))
    print("</table>")


s = "Aardvarks are eating my lunch"
print("mungeChars(%s) = %s" % (s, mungeChars(s)))

inPipe = open("Creator.html", "r")
s = inPipe.read()
print("mungeLetter(%s) = %s" % ("Creator.html", mungeLetter(s)))

print("makeTable(mungeletter(%s)) = %s" % ("Creator.html", makeTable(mungeLetter(s))))
