print("Welcome to my Game!")

playing = input("Do you want to Play!: ")
if playing.lower() != 'yes':
    quit()

print("Let's Play :) ")
score = 0

answers = input("What is the fullform of WWW ")
if answers.lower() == 'world wide web':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answers = input("What is the fullform of HTTP ")
if answers.lower() == 'hypertext transfer protocol':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answers = input("What does HTML stands for ")
if answers.lower() == 'hypertext markup language':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answers = input("What is the full form of SSD ")
if answers.lower() == 'solid state drive':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answers = input("What does CPU stands for ")
if answers.lower() == 'central processing unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answers = input("What does CSS stands for ")
if answers.lower() == 'cascading style sheet':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answers = input("What does GPU stands for ")
if answers.lower() == 'graphics processing unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answers = input("What does PSU stands for ")
if answers.lower() == 'power supply unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answers = input("What does RAM stands for ")
if answers.lower() == 'random access memory':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answers = input("What does ROM stands for ")
if answers.lower() == 'read only memory':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " answers correct!")
print("Thankyou for playing the game :)")