def printList(num):
    if num == []:
        return 
    first = num[0]
    rest = num[1:]
    print(first)
    printList(rest)
    

def printListBackwards(num):
    if not num:
        return 
    first = num[0]
    rest = num[1:]
    printListBackwards(rest)
    print(first)


x = range(10)
printList(x)
y = ["a", "b", "c"]
printListBackwards(y)
