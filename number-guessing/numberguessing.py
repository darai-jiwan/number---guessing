import random 

game = True 
while game == True :
    level = input("choose your level (easy/medium /hard): ").lower()
    if level == "easy":
        count = 5
        number = random.randint(1,20)
        while count >0:
            guess = int (input("Guess a number between 1-20:"))
            if number == guess:
                print("You are Correct")
                game = False
                break
            elif guess< number:
                print("higher")
                count -=1
            elif guess > number:
                print("lower")
                count -=1

            else: 
                print("Enter a interger value")
        print(f"The correct number is {number}")

    elif level =="medium":
        count = 7
        number = random.randint(1,50)
        while count >0:
            guess = int (input("Guess a number between 1-50:"))
            if number == guess:
                print("You are Correct")
                game = False
                break
            elif guess< number:
                print("higher")
                count -=1
            elif guess > number:
                print("lower")
                count -=1

            else: 
                print("Enter a interger value")
        print(f"The correct number is {number}")


    elif level =="hard":
        count = 10
        number = random.randint(1,100)
        while count > 0:
            guess = int (input("Guess a number between 1-100:"))
            if number == guess:
                print("You are Correct")
                game = False
                break
            elif guess< number:
                print("higher")
                count -=1
            elif guess > number:
                print("lower")
                count -=1

            else: 
                print("Enter a interger value")
        print(f"The correct number is {number}")

    else: 
        print("Choose a correct option (easy/ medium/ hard)")

