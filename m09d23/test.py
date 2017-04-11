import kelmore5.python.morrison.intro.m09d23.PrePostConditions as PrePostConditions

a = input("Enter a side length:  ")
b = input("Enter a side lenght:  ")

print("The right triangle you specified with legs of length")
print("%s and %s has third side of length %s" % (a, b, PrePostConditions.hypot(a, b)))
