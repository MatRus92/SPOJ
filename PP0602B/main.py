import fileinput


while True:
    for t in range(int(input())):
        for _ in range(t + 1):
            lk = input()
            l = int(lk[0])
            k = int(lk[-1])

            lines = ''
            #lines = '1 2 3 4 '
            #lines += '5 6 7 8 '
            #lines += '9 0 A B '
            #lines += 'C D E F '
            #lines += 'G H I J '
            for _ in range(int(l)):
                lines += input() + ' '

            linesArr = [lines[i:i+(k*2) - 1] for i in range(0, len(lines), (k*2))]

            linesCenters = [linesArr[i] for i in range(1, len(linesArr) - 1)]

            linesFrame = str(linesArr[0])
            fir = ''.join([str(linesCenters[i][-1]) for i in range(0, len(linesCenters))])
            linesFrame += ' ' + fir

            linesFrame += ' ' + linesArr[-1][::-1]

            fir = ' '.join([str(linesCenters[i][0]) for i in range(0, len(linesCenters))][::-1])
            linesFrame += ' ' + fir
            linesFrame = linesFrame[2:] + ' ' + linesFrame[:2]
            linesFrame = linesFrame.replace(' ', '')

            finishLines = linesFrame[:k] + ' ' + linesFrame[-(k+l-2):-(l-2)][::-1]
            print(linesArr)
            print(linesCenters)
            print(linesFrame)
            print(finishLines)

    break
print('koniec')




