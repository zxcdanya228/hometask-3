queue_ = []

while True:
    command = input().strip()
    if command.startswith('push'):
        number = int(command.split()[1])
        queue_.append(number)
        print('ok')
    elif command == 'pop':
        print(queue_.pop(0))
    elif command == 'back':
        print(queue_[-1])
    elif command == 'size':
        print(len(queue_))
    elif command == 'clear':
        queue_.clear()
        print('ok')
    elif command == 'exit':
        print('bye')
        break
    else:
        print('error')