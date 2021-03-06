import gspread
from google.oauth2.service_account import Credentials
import json
import time
import getpass
from HelperMethods import HelperMethods
from CalcFunctions import CalcFunctions


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Deco_Table')

Sheet1 = SHEET.worksheet('Sheet1')

data = Sheet1.get_all_values()


def landing_page():
    """
    First page the user interracts with
    """
    print("\n")
    print("\n-------------------------------------------------\n")
    print("Buehlmann Tables for Air Diving Decompression")
    print("\n-------------------------------------------------\n")
    user_name = input("Please enter your name:\n")
    print("\n")
    print(f"Welcome to the Buehlmann Tables {user_name}")
    time.sleep(2)
    print("\n")
    input("\nTo proceed, press Enter\n")
    time.sleep(2)
    main_menu()


helper = HelperMethods()
calculations = CalcFunctions()


def main_menu():
    """
    Runs main welcome message and optional branches
    """
    print("\n")
    print("\n")
    print("\n")
    print('\nWelcome to the Buehlmann Table for Air Diving Decompression\n')
    time.sleep(1.5)
    print('This calculator will provide you with the means to;\ncalculate your decompression times or plan a dive\n')
    time.sleep(1.5)
    print('You can also access information about the Buehlmann Table and why it was created\n')
    time.sleep(1.5)
    print('Would you like to read some information about dive tables?\nMake a dive plan?\nOr calculate your deco stops?\n')
    time.sleep(1.5)
    while True: 
        options_main = input('For information type "info"\nFor dive planning type "plan"\nFor deco stop calculation type "deco"\nOr to exit type "exit"\n')
        if options_main.lower() == "info":
            print("\n")
            print("\nYou have selected to view the information page\n")
            print("\n")
            time.sleep(1)
            helper.info_on_tables()
        elif options_main.lower() == "plan":
            print("\n")
            print("\nYou have selected to visit the dive planning page\n")
            print("\n")
            time.sleep(1)
            helper.dive_planning()
        elif options_main.lower() == "deco":
            print("\n")
            print("\nYou have selected to visit the deco stop calculation page\n")
            print("\n")
            time.sleep(1)
            deco_calculator()
        elif options_main.lower() == "exit":
            time.sleep(1)
            landing_page()
            break
        else:
            print("\n")
            print("\nInvalid input, please try again\n")
            print("\n")


def deco_calculator():
    """
    Requests diver to input their depth and time
    """
    inputedDepth = 0
    inputtedMins = 0

    print("\n")
    time.sleep(2)
    print('\nUse this page to calculate if a decompression stop is \nneeded for a given depth and time\n')
    
    start = input('Would you like to start a calculation y/n')
    if start.lower() == 'y':
        while True:
            try:
                inputtedDepth = int(input("Depth:"))
                print(f"Depth of {inputtedDepth} meters")
                break
            except ValueError:
                print("Please input a number only")
                continue
        while True:
            try:
                inputtedMins = int(input("Time:"))
                print(f"Time of {inputtedMins} minutes")
                break
            except ValueError:
                print("Please input a number only")
                continue
        calculations.calculate_deco(inputtedMins, inputtedDepth)     
    elif start.lower() == 'n':
        print("\nReturning to main menu\n")
        time.sleep(2)
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        main_menu()
    else:
        print("\n")
        print("\nInvalid input, please try again")
        print("\n")
        deco_calculator()

   
landing_page()
