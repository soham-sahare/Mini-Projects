command = ""
started = False
print("Enter the 'HELP'")
while command.lower() != "quit":
    command = input("> ").lower()
    if command.lower()=="start":
        if started:
            print("Car already Started")
        else:
            started=True
            print("Car startedd......")
    elif command.lower()=="stop":
        if not started:
            print("Car is already Stopped")
        else:
            started = False
            print("Car Stopped!!")
    elif command.lower()=="help":
        print("""
            start - to START the car
            stop - to STOP the car
            quit - to QUIT 
            """)
    elif command.lower()=="quit":
        break
    else:
        print("I dont understand.......")
