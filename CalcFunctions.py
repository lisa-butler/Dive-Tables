import json
from google.oauth2.service_account import Credentials
from HelperMethods import HelperMethods
import gspread
import time

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


class CalcFunctions(object):


    def calculate_deco(self, inputtedMins, inputtedDepth):
        """
        Function to calculate deco stop and what depth it is needed at 
        """

        helper = HelperMethods()
        data = helper.get_data()

        if int(inputtedMins) > 125 or int(inputtedDepth) > 51:
            print('''Buehlmann tables do not support depths exceeding 51m and
             dives exceeding 125 minutes, please try again''')    
        else:
            for row in data:
                if row[0] != "meters":
                    if int(inputtedDepth) <= int(row[0]):
                        if int(inputtedMins) <= int(row[1]):
                            if int(row[2]) == 0:
                                # return "No Deco Needed"
                                print("\n----------------------------")
                                print("Stops Required:")
                                print("No decompression stop needed")
                                print("----------------------------\n")
                                time.sleep(2)
                                input("\nTo return to main menu hit Enter")
                                time.sleep(2)
                                print("\nReturning to main menu\n")
                                time.sleep(2)
                                print("\n")
                                time.sleep(1)
                                print("\n")
                                time.sleep(1)
                                print("\n")
                                time.sleep(2)
                                print("\n")
                                break
                            else:
                                three_stop = row[2]
                            if int(row[3]) == 0:
                                # return 3m_stop
                                print("\n---------------------------")
                                print("Stops Required:")
                                print(f'3 meter stop for {three_stop} minutes')
                                print("---------------------------\n")
                                time.sleep(2)
                                input("\nTo return to main menu hit Enter")
                                time.sleep(2)
                                print("\nReturning to main menu\n")
                                time.sleep(2)
                                print("\n")
                                time.sleep(1)
                                print("\n")
                                time.sleep(1)
                                print("\n")
                                time.sleep(2)
                                print("\n")
                                break
                            else:
                                six_stop = row[3]
                            if int(row[4]) == 0:
                                # return 3m_stop and 6m_stop
                                print("\n---------------------------")
                                print("Stops Required:")
                                print(f'3 meter stop for {three_stop} minutes')
                                print(f'6 meter stop for {six_stop} minutes')
                                print("----------------------------\n")
                                time.sleep(2)
                                input("\nTo return to main menu hit Enter")
                                time.sleep(2)
                                print("\nReturning to main menu\n")
                                time.sleep(2)
                                print("\n")
                                time.sleep(1)
                                print("\n")
                                time.sleep(1)
                                print("\n")
                                time.sleep(2)
                                print("\n")
                                break
                            else:
                                nine_stop = row[4]
                            if int(row[4]) != 0:
                                print("\n---------------------------")
                                print("Stops Required:")
                                print(f'3 meter stop for {three_stop} minutes')
                                print(f'6 meter stop for {six_stop} minutes') 
                                print(f'9 meter stop for {nine_stop} minutes')
                                print("----------------------------\n")
                                time.sleep(2)
                                input("\nTo return to main menu hit Enter")
                                time.sleep(2)
                                print("\nReturning to main menu\n")
                                time.sleep(2)
                                print("\n")
                                time.sleep(1)
                                print("\n")
                                time.sleep(1)
                                print("\n")
                                time.sleep(2)
                                print("\n")
                                break
                        elif int(inputtedMins) > int(row[1]):
                            print("\n")
                            time.sleep(2)
                            print("\nMax time for this depth exceeded\n")
                            input("\nTo return to main menu hit Enter")
                            time.sleep(2)
                            print("\nReturning to main menu\n")
                            time.sleep(2)
                            print("\n")
                            time.sleep(1)
                            print("\n")
                            time.sleep(1)
                            print("\n")
                            time.sleep(2)
                            print("\n")

                            break      
