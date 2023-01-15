command = ""
while command != "quit":
	command = input("> ").lower()
	if command == "quit":
	    print("done") 
	elif command == "start":
		print("starting...")
	else:
		print("heyo")