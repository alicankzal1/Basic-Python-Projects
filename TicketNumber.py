
import random
count = 0

print("Welcome")
sira = input("Do you want to a ticket number ? (y/n)")

while sira.lower() == "y":
   
    count+=1
    last_name = input(" last name ? ")
    name = input(" name ? ")

    print(" Welcome " + name.capitalize() + " " + last_name.capitalize() + " your queue is = " + str(count))
    sira = input(" Do you want to a ticket number ? (y/n) ")



