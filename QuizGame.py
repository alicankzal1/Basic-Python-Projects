print("welcome my quiz game")

playing = input("Do you wanna play ? ")

if playing.lower() != "yes" :
    quit()

print("Okay ! Let's play :) ")
score = 0
answer = input("What is my name ? ")
if answer.lower() == "ali can":
    print("correct ! ")
    score += 1
else:
    print("incorrect :( ")

answer = input("what is my last name ?")
if answer.lower() == "kızal":
    print("correct ! ")
    score += 1
else:
    print("incorrect :( ")

print("you got " + str(score) + " question correct")
print("You got " + str((score / 2) * 100) + " %. ")

