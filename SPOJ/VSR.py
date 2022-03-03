numberOfAttempts = input()
returns = []

for x in range(0, int(numberOfAttempts)):
    speeds = input()
    speedA = speeds.split( )[0]
    speedB = speeds.split( )[1]

    returns.append(2 * int(speedA) * int(speedB) / (int(speedA) + int(speedB)))

for y in range(len(returns)):
    print(int(returns[y]))