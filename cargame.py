command = ""
while command != "quit":
  command = input("> ").lower()
  if command == "start":
    print("starting...")
  elif command == "stop":
    print("pause")
  elif command == "help":
    print('''
    start   start playing your game
    stop    pause the game
    quit    exit game
    ''')
  elif command == "quit":
    break
  else:
    print("sorry, i dont understand")
    
  
  
  
  
