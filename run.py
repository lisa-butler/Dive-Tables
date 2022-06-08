import gspread
from google.oauth2.service_account import Credentials
import json
import time
import getpass
from HelperMethods import HelperMethods
from CalcFunctions import CalcFunctions

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
# ]

# CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('Deco_Table')

# Sheet1 = SHEET.worksheet('Sheet1')

# data = Sheet1.get_all_values()


# #print(data[0][1])
# inputtedDepth = 0
# inputtedMins = 0
# three_stop = ""
# six_stop = ""




def landing_page():
    """
    First page the user interracts with
    """

    print("\nBuehlmann Tables for Air Diving Decompression\n")
    user_name = getpass.getpass("Please enter your name:\n")
    print(f"Welcome to the Buehlmann Tables {user_name}")
    input("\nTo proceed, press Enter\n")
    time.sleep(2)
    main_menu()

helper = HelperMethods()
calculations = CalcFunctions()

def main_menu():
    """
    Runs main welcome message and optional branches
    """
    print('Welcome to the Buehlmann Table for Air Diving Decompression\n')
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
            print("You have selected to view the information page")
            print("\n")
            helper.info_on_tables()
        elif options_main.lower() == "plan":
            print("You have selected to visit the dive planning page")
            helper.dive_planning()
        elif options_main.lower() == "deco":
            print("You have selected to visit the deco stop calculation page")
            print("\n")
            deco_calculator()
        elif options_main.lower() == "exit":
            break
        else:
            print("Invalid input, please try again")
            print("\n")



def deco_calculator():
    """
    Requests diver to input their depth and time
    """

    print('You have selected to calculate if a decompression stop is needed for a given depth and time\n')
    start = input('Would you like to start a calculation y/n')
    if start.lower() == 'y':
        inputtedDepth = input('Depth:')
        inputtedMins = input('Time:')

        print(f"Depth of {inputtedDepth} meters")
        print(f"Time of {inputtedMins} minutes")


        calculations.calculate_deco(inputtedMins, inputtedDepth)


landing_page()