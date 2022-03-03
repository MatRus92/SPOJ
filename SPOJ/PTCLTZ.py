numberOfAttempts = input()
returns = []

for x in range(0, int(numberOfAttempts)):
    i = 0
    xn = int(input())

    while True:
        if xn == 1:
            break
        else:
            if xn % 2 == 0:
                xn = xn / 2
            else:
                xn = 3 * xn + 1
        i += 1

    print(i)