command = ""
started = False
while command != "quit":
    command = input('> ').lower()
    if command == "start":
        if started:
            print('car is already started')
        else:
            started = True
            print('car started...Ready to go!')
    elif command == "help":
        print('''
        start     to start the car
        stop      to stop the car
        quit       to end the game
        ''')
    elif command == "stop":
        if not started:
            print('car has already stopped')
        else:
            started = False
        print('car stopped.')
    elif command == "quit":
        break
    else:
        print('I dont understand')
 