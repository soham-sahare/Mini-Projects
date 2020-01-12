import random;
command = ""
points=0
chance = 0
started = False
print("SLOT GAME")
chance_limit = input("Enter the number of chances you want to play :")
print("Enter 'SLOT' for MENU")
while command.lower != 'quit' and chance < int(chance_limit):
    command = input("> ").lower()
    if command.lower()=='start':
        secret_number1 = random.randint(0, 9)
        secret_number2 = random.randint(0, 9)
        secret_number3 = random.randint(0, 9)
        print(f'{secret_number1}  '
              f'{secret_number2}'
              f'  {secret_number3}')
        if (secret_number1 == secret_number2) or (secret_number2 == secret_number3) or (secret_number3 == secret_number1):
            points += 2
        elif (secret_number1 == secret_number2) and (secret_number2 == secret_number3) and (secret_number3 == secret_number1):
            points +=5
        else:
            points +=1
        chance +=1
    elif command.lower()=='slot':
        print("""
        Start - To start the game
        Stop - To stop the game
        Quit - To Exit
        """)
    elif command.lower() =='quit':
        break
    elif command.lower() == 'stop':
        print("stopped")
    else:
        print("I didn't understood.......Sorry!")
print(f'YOUR FINAL SCORE IS {points}')