from random import randint

choice = -1
print("\nDice Rolling Simulator :-")

while(choice != 0):
    
    print("\n1) Roll The Single Dice")
    print("2) Roll The Double Dice")
    print("0) Exit")
    
    choice = int(input("\n_ : "))
    
    if(choice == 1):
        print("\nDice 1 =",randint(1,6))
        print("Dice 2 =",randint(1,6))
    elif(choice == 0):
        print("\nExited -")
    else:
        print("\nInvalid Input -")