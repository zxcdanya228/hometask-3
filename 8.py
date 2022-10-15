stack = []

while True:
    command = input().strip()
    if command.startswith('push'):
        number = int(command.split()[1])
        stack.append(number)
        print('ok')
    elif command == 'pop':
        print(stack.pop())
    elif command == 'back':
        print(stack[-1])
    elif command == 'size':
        print(stack)
    elif command == 'clear':
        stack.clear()
        print('ok')
    elif command == 'exit':
        print('bye')
        break
    else:
        print('error')