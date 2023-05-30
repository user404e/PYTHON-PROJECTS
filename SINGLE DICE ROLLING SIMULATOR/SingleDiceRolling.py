from random import randint

choice = -1
print("\nDice Rolling Simulator :-")
while(choice != 0):
    print("\n1) Roll The Dice")
    print("0) Exit")
    
    choice = int(input("\n_ : "))
    
    if(choice == 1):
        print("\nDice =",randint(1,6))
    elif(choice == 0):
        print("\nExited -")
    else:
        print("\nInvalid Input -")