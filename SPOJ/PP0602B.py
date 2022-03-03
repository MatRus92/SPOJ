import sys

try:
    while True:
        for t in range(int(input())):
            for _ in range(t + 1):
                lk = input()
                l = int(lk.split(' ')[0])
                k = int(lk.split(' ')[1])

                if l < 3 or k > 100:
                    sys.exit(0)

                lines = []
                for _ in range(int(l)):
                    lines.append(input().split(' '))

                linesArr = [' '.join(lines[i]) for i in range(0, len(lines))]

                frameRotated = []
                for i in range(l):
                    if i == 0:
                        frameRotated.append(
                            ' '.join(linesArr[0].split(' ')[1:]) + ' ' + str(linesArr[1].split(' ')[1:][-1]))
                    elif i == l - 1:
                        frameRotated.append(
                            ' '.join(linesArr[i - 1].split(' ')[:1]) + ' ' + ' '.join(
                                linesArr[i].split(' ')[:k - 1][:k - 1]))
                    else:
                        frameRotated.append(
                            linesArr[i - 1].split(' ')[0] + ' ' + ' '.join(linesArr[i].split(' ')[1:-1]) + ' ' +
                            linesArr[i + 1].split(' ')[-1])

                for i in range(len(frameRotated)):
                    print(frameRotated[i])

        sys.exit(0)
except:
    sys.exit(0)
