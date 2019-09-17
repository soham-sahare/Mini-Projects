import random;
name=input("What is your name?")
print(name+" Welcome to the Guessing game")
print("You have to guess the number from 1 to 9 while you have only 3 chances ")
print("Best Of Luck1!!!")

print('Enter the number from 0 to 9')
for x in range(1):
    secret_number = random.randint(0,9)
guess_count = 0
guess_limit = 3
chances = 3
i=3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You WON!!')
        break
else:
    print('You LOSE!!')
    print('Better luck Next Time')
print(f'The number is {secret_number}')
