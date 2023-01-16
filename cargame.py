command = ""
while command != "quit":
    command = input('> ').lower()
    if command == "start":
        print('car started...Ready to go!')
    elif command == "help":
        print('''
        start     to start the car
        stop      to stop the car
        quit       to end the game
        ''')
    elif command == "stop":
        print('car stopped.')
    elif command == "quit":
        break
    else:
        print('I dont understand')
 