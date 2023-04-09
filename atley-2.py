"""
Title: Introduction to Information Technology,  Assignment 1
Task: Challenge 2
Author: Billy Atley
Status: Final
Type: University Assignment
Created: 01-Apr-2023
Python Version: 3.x
"""

import os
import sys
import time

ts = os.get_terminal_size()
INDENT = "\t"

# Values for hand caculations as dictionaries
C2 = {"Coefficient":0.35, "Height":1}

def menu():
    os.system("cls")
    print(ts.lines * "\n")

    print(" " * 14 + "\033[1;33mUniversity of Canberra\033[0;0m")
    print(" " * 5 + "Introduction to Information Technology")
    print(" " * 14 + "Semester 1, 2023\n")
    print(" " * 16 + "Assignment 1\n\n")

    print(INDENT + "Billy Atley")
    print(INDENT + "u3255837\n\n")    
    print(INDENT + "\033[1;34m\t\n\nAssignment 1\n\n")
    print(INDENT + "Challenge 2\033[0;0m\n")
    print(INDENT + "Use the keyboard to...")
    print(INDENT + "[1] Calculate how many times a ball bounces before the bounce is less than 10cm. " )
    print(INDENT + "[2] Calculate the distance travelled by a ball before its bounce is less than 10cm. ")
    print(INDENT + "[3] Present the results for the hand calculation submitted in the assignment.")
    print(INDENT + "[4] Quit.\n\n")
    while True:
        try:
            selection = int(input("Enter a selection "))
            if selection == 1:
                presentBounces()
            elif selection == 2:
                presentDistanceTravelled()
            elif selection == 3:
                presentExample()
            elif selection == 4:
                print("\t\t\tBye.")
                sys.exit()
            else:
                print("Invalid")
                main()
        except ValueError:
            os.system("cls")
            print("\n" * 5 + "Another Invalid choice")
            main()


def presentBounces():
    """
    Gathers the data to submit to calculateBounces() and present the
    results with the object returned to the user

    Args:
        None

    Returns:
        Nothing

    """

    while True:
        try:
            coeffRestitution = float(input("Enter a coefficient of restitution, between 0 and 1: "))
            if 0 <= coeffRestitution <= 1:
                break
            else:
                print(f"You entered {coeffRestitution}. This coefficient of restitution does not belong in this Universe,\
                      \n enter a number between 0 and 1!")
                continue
        except ValueError:
            print(f"You entered an invalid input. Enter a decimal number between 0 and 1.")

    while True:
        try:
            height = float(input("Enter the height from which the ball is dropped: "))
            break
        except ValueError:
            print(f"You entered an invalid input. Enter a decimal number.")

    calcBounces = calculateBounces(coeffRestitution, height)

    print(f"\n\033[1;33mThe number of bounces of a ball dropped from a height of {height}m with a coefficient of {coeffRestitution} is {calcBounces}.\033[1;0m")

    input("\nPress any key to continue...u")
    menu()

def presentExample():
    """
    Function to deliver the results from the fixed variables used in the hand calculations. 
    
    """
    exBounces = calcBounces = calculateBounces(C2["Coefficient"], C2["Height"])
    exDistanceTravelled = calculateDistanceTravelled(C2["Coefficient"], C2["Height"])

    height = C2["Height"]
    coefficient = C2["Coefficient"]

    # for some reason splitting the line into two lines does not work.
    print(f"\n\033[1;33mThe example of a ball dropped from a height of {height}m with a coefficient of restitution of {coefficient}  will bounce {exBounces} times and travel {exDistanceTravelled}m before its bounce falls below 10cm.\033[0;0m")


    input("\nEnter anything to return to the Menu ")
    menu()

# Functions for Challenge 2
def calculateBounces(coefficientRestitution, initialHeight):
    """
    Calculates number of bounces a ball makes when dropped from a fixed height until
    its bounce falls below 10cm

     Args:
         coefficientRestitution (float): The face value of the bond
         initialHeight (float): The current market price of the bond

     Returns:
         int: The number of bounces.

    """
    height = initialHeight
    bounces = 0
    while height >= 0.1:
        height *= coefficientRestitution
        bounces += 1
    return bounces


def presentDistanceTravelled():
    """
    Gathers the data to submit to calculateDistanceTravelled() and present it to the user.
         
    Args:
        None

     Returns:
         Nothing
    """

    while True:
        try:
            coeffRestitution = float(input("Enter a coefficient of restitution betwen 0 and 1: "))
            print(f"You entered {coeffRestitution}")
            break
        except  ValueError:
            print(f"You entered {coeffRestitution}. Something betwen 0 and 1, remember?")

    while True:
        try:
            height = float(input("Enter the heigfht from which the ball is dropped "))
            print(f"You entered {height}")
            break
        except:
            ValueError
        print(f"You entered {height}. Enter a number, even a decimal number")
    calcDist = calculateDistanceTravelled(coeffRestitution, height)
    print(f"\033[1;33mA ball dropped from a height of {height} with a coefficient of restitution of {coeffRestitution} will travel {calcDist}m before its bounce falls below 10cm.\033[0;0m\n")

    input("Enter anything to return to the Menu")
    menu()


def calculateDistanceTravelled(coefficientRestitution, initialHeight):
        """
        Calculates the distance travelled by a ball makes when dropped from a fixed height until
        its bounce falls below 10cm

        Args:
            coefficientRestitution (float): The face value of the bond
            initialHeight (float): The initial height of the ball

        Returns:
            float: The number of bounces.

        """
        bounces = calculateBounces(coefficientRestitution, initialHeight)

        distance = initialHeight

        for i in range(1, bounces):
            # print('i = ', i)
            distance += 2 * (initialHeight * (coefficientRestitution**i))  # See assignment for more info
        return round(distance, 2)



def calculateFormulaA(faceValueBond, currentMarketPrice, yearsToMaturity):
    """
    Calculates the parameter a in the formula for the approximate yield to maturity of a bond.
               ytm = (intr + a)/b

    Args:
        faceValueBond (float): The face value of the bond
        currentMarketPrice (float): The current market price of the bond
        yearsToMaturity (int): The number of terms to sum.

    Returns:
        float: the value of the parameter.
    """
    formulaA = (faceValueBond - currentMarketPrice) / yearsToMaturity
    return formulaA

def calculateFormulaB(faceValueBond, currentMarketPrice):
    """
    Calculates the parameter b in the formula for the approximate yield to maturity of a bond.
               ytm = (intr + a)/b

    Args:
        faceValueBond (float): The face value of the bond
        currentMarketPrice (float): The current market price of the bond
        yearsToMaturity (int): The number of terms to sum.

    Returns:
        float: the value of the parameter.
    """

    formulaB = (faceValueBond + currentMarketPrice) / 2  ##formulaB
    return formulaB


def main():
    menu()

if __name__ == "__main__":
    # code to be executed when the program is run as the main program goes here
    main()
