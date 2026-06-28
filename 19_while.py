#while condition:
    #statements

pin = input("Enter ATM pin ")

count = 0
while pin != "1234" and count < 3:
    print("Invalid pin entered")
    pin = input("Try again with right pin ")
    count += 1
