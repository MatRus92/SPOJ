def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    element = int(n ** 0.5) + 1
    for i in range(3, element, 2):
        if n % i == 0:
            return False
    return True


for i in range(int(input())):
    n = int(input())

    if czy_pierwsza(n):
        print("TAK")
    else:
        print("NIE")
