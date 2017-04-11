outPipe = open("Resuls.finkelstein", "a")
n = int(input("Enter a number:  "))
iters = 1
total = 0

while iters <= n:
    total += iters ** 2
    iters += 1
print(total)
outPipe.write("The sum of squares is to %s is %s\n" % (n, total))
