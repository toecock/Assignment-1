"""
Title: Introduction to Information Technology,  Assignment 1
Task: Challenge 1
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

C1 = {"FaceValue":2000, "CouponInterestRate": 0.09, "CurrentMarketPrice":2500, "Years":8}

def menu():
    os.system("cls")
    print(ts.lines * "\n")

    print(" " * 14 + "\033[1;33mUniversity of Canberra\033[0;0m")
    print(" " * 5 + "Introduction to Information Technology")
    print(" " * 14 + "Semester 1, 2023\n")
    print(" " * 16 + "Assignment 1\n\n")

    print(INDENT + "Billy Atley")
    print(INDENT + "u3255837\n\n")    
    print(INDENT + "\033[1;32m\t\n\nAssignment 1\n\n")
    print(INDENT + "Challenge 1\033[0;0m\n")
    print(INDENT + "Use the keyboard to...")
    print(INDENT + "[1] Calculate the Approximate Yield to Maturity of a Bond. " )
    print(INDENT + "[2] Present the results for the hand calculation submitted in the assignment.")
    print(INDENT + "[3] Quit.\n\n")
    while True:
        try:
            selection = int(input("Enter a choice "))
            if selection == 1:
                presentYTM()
            elif selection == 2:
                presentExample()
            elif selection == 3:
                print("\t\t\tBye.")
                sys.exit()
            else:
                print("Invalid")
                main()
        except ValueError:
            os.system("cls")
            print("\n" * 5 + "Another Invalid choice")
            main()


def presentYTM():
    """
    Gathers the data to submits it  to calculateBounces() and presents
     the results with the object returned from this function. 

    Args:
        None

    Returns:
        Nothing

    """

    while True:
        try:
            faceValue = int(input("Enter the face value for a bond "))
            print(f"You entered {faceValue}")
            break
        except ValueError:
            print(f"You entered {faceValue}. Enter a whole number")

    while True:
        try:
            couponInterestRate = float(input("Enter the coupon interest rate for a bond "))
            print(f"You entered {couponInterestRate}")
            break
        except ValueError:
            print(f"You entered {couponInterestRate}. Enter a number, even a decimal number")

    while True:
        try:
            marketPrice = float(input("Enter the current market price for a bond "))
            print(f"You entered {marketPrice}")
            break
        except ValueError:
            print(f"You entered {marketPrice}. Enter a number, even a decimal number")

    while True:
        try:
            years = float(input("Enter the years to maturity for the a bond "))
            print(f"You entered {years}")
            break
        except ValueError:
            print(f"You entered {years}. Enter a number, a positive whole number.")

    intr = calculateIntr(faceValue, couponInterestRate)

    a = calculateFormulaA(faceValue, marketPrice, years)

    b = calculateFormulaB(faceValue, marketPrice)

    calcYTM = calculateYTM(intr, a, b)
    y = int(years)

    percent = f"{couponInterestRate:.1%}"

    # too many attempts at trying to get this to work as  muliline print statement. Cie la vie.
    print(f"\n\033[1;33mA bond with a face value of {faceValue} dollars, a coupon interest rate of {percent} and a current market price of {marketPrice} with {years} years remaining has a calculated approximate yield to maturity of {calcYTM}.\033[0;0m")

    input("\nPress any key to continue...u")
    main()

def presentExample():
    """
    Function to deliver the results from the fixed variables used in the hand calculations. 
    
    """
    fValue = C1["FaceValue"]
    cInterestRate  = C1["CouponInterestRate"]
    cMarketPrice = C1["CurrentMarketPrice"]
    years = C1["Years"]

    intr = calculateIntr (fValue, cInterestRate)

    a = calculateFormulaA(fValue, cMarketPrice, years)

    b = calculateFormulaB(fValue, cMarketPrice)

    calcYTM = calculateYTM(intr, a, b)
    
    # None of these f-string formatting apepeared in the following printf statement. Extrracting them from the dictionary did something. 
    # percent2 = f"{cInterestRate:.1%}"
    # cMP = f"{cMarketPrice:.0}"
    # y = f"{years:.0}"

    # for some reason attempting to split this into a multline print statement fails, miserably,
    print(f"\n\033[1;33mThe example of a bond with a face value of {fValue} dollars, an interest rate of {cInterestRate} and a current market price of {cMarketPrice} dollars with {years} remaining has a calculated approximate yield to maturity of {calcYTM}\033[0;0m")
   
    input("\nPress any key to continue..")
    menu()


def calculateYTM(intr, formulaA, formulaB):
    """
    Calculate the approximate yield to maturity for a bond according to the equation
              ytm = (intr + a)/b
    Args:
        faceValueBond (float): The face value of the bond
        currentMarketPrice (float): The current market price of the bond
        yearsToMaturity (int): The number of terms to sum.

    Returns:
        float: the value of the parameter.
    """
    ytm = (intr + formulaA) / formulaB
    percentage = "{:.1%}".format(ytm)
    return percentage

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

def calculateIntr(faceValueBond, couponInterestRate):
    """
    Calculates the annual interst payment for a bond for a coupon interest rates

    Args:
        faceValueBond (float): the face value of the bond
        couponInterestRate (float)

    Returns:
        float: the interest payment

    """
    interestRate = faceValueBond * couponInterestRate
    return interestRate

def main():
    menu()

if __name__ == "__main__":
    # code to be executed when the program is run as the main program goes here
    main()
