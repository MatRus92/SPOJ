for i in range(int(input())):
    if 0 < i + 1 < 31:
        n = int(input())

        if n < 2:
            print("0 1")
        elif n == 2:
            print("0 2")
        elif n == 3:
            print("0 6")
        elif n == 4:
            print("2 4")
        elif n == 5:
            print("2 0")
        elif n == 6:
            print("2 0")
        elif n == 7:
            print("4 0")
        elif n == 8:
            print("2 0")
        elif n == 9:
            print("8 0")
        else:
            print("0 0")
    else:
        break
