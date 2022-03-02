import math
import sys

try:
    while True:
        for t in range(int(input())):
            for _ in range(t + 1):
                lk = input()
                l = int(lk.split(' ')[0])
                k = int(lk.split(' ')[1])

                if l < 3 or l > 101:
                    break

                lines = ''
                numerator = 1
                for i in range(int(l)):
                    for j in range(int(k)):
                        if numerator == 10:
                            lines += '0 '
                            numerator = 1
                        else:
                            lines += str(numerator) + ' '
                            numerator += 1

                linesArr = [lines[i:i + (k * 2) - 1] for i in range(0, len(lines), (k * 2))]

                linesCenters = [linesArr[i] for i in range(1, len(linesArr) - 1)]

                linesFrame = str(linesArr[0])
                fir = ''.join([str(linesCenters[i][-1]) for i in range(0, len(linesCenters))])
                linesFrame += ' ' + fir

                linesFrame += ' ' + linesArr[-1][::-1]

                fir = ' '.join([str(linesCenters[i][0]) for i in range(0, len(linesCenters))][::-1])
                linesFrame += ' ' + fir
                linesFrame = linesFrame[2:] + ' ' + linesFrame[:2]
                linesFrame = linesFrame.replace(' ', '')

                finishLines = []
                finishLines.append(" ".join(linesFrame[:k]))

                rangeLen = int(math.ceil(len(linesFrame) / k + 1) - 2)

                if l > 9:
                    rangeLen += 1

                for i in range(rangeLen):
                    if len(finishLines) < l - 1 and \
                            (l < 4 or (linesFrame[k + i:k + i + 1] != '' and linesFrame[
                                                                             (2 * k + i + (k - 1)):(
                                                                                     2 * k + i + k)] != '')):
                        finishLines.append(
                            linesFrame[len(linesFrame) // 2:][::-1][i] + linesArr[i + 1][1:-1] + linesFrame[
                                                                                                 k + i:k + i + 1])

                finishLines.append(" ".join(linesFrame[-(k + l - 2):-(l - 2)][::-1]))

                for i in range(len(finishLines)):
                    print(finishLines[i])

        sys.exit(0)
except:
    sys.exit(0)
