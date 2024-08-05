print(("welcome to my computer quiz game!!"))


#asking if user want to play or not
playing = input("Do you want to play??")
if playing.lower() is "yes":
    quit()
print("okay let's play :)")
score = 0


#starting the game
answer = input("what is the full form of CPU?\n")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what is the full form of GPU?\n")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what is the full form of RAM?\n")
if answer.lower() == "random acess memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what is the full form of PSU?\n")
if answer.lower() == "power supply unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

#results
print("You got "+ str(score) +" questions correct!")
print ("you got "+ str((score/4)*100)+"%.")