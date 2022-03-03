returns = []
stack = []


while True:

    try:
        character = input()
    except EOFError:
        break

    if (character == "+"):
        if (len(stack) < 10):
            try:
                character = input()
            except EOFError:
                break
            stack.append(character)
            print(':)')
        else:
            try:
                character = input()
            except EOFError:
                break
            print(':(')
    else:
        if (len(stack) > 0):
            print(stack.pop())
        else:
            print(':(')