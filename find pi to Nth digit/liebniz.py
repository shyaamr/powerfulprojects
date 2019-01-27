pi = 0
repeat = input("Accuracy ?")
repeatInt = int(repeat)

for i in range(0, repeatInt):
    pi += ((4.0 * (-1)**i) / (2*i + 1))
    print(pi)
