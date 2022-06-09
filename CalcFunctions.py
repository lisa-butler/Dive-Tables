import json
from google.oauth2.service_account import Credentials
from HelperMethods import HelperMethods
import gspread

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

        helper = HelperMethods()
        data = helper.get_data()

        if int(inputtedMins) > 125 or int(inputtedDepth) > 51:
            print("Buehlmann tables do not support depths exceeding 51m and dives exceeding 125 minutes, please try again")
        else:
            for row in data:
                if row[0] != "meters":
                    # print(int(row[0]))
                    if int(inputtedDepth) <= int(row[0]):
                        # print(row[1])
                        if int(inputtedMins) <= int(row[1]):
                            # print(row[2])
                            if int(row[2]) == 0:
                                # return "No Deco Needed"
                                print("No decompression stop needed")
                                break
                            else:
                                three_stop = row[2]
                            if int(row[3]) == 0:
                                # return 3m_stop
                                print(f'3m stop for {three_stop}mins')
                                break
                            else:
                                six_stop = row[3]
                            if int(row[4]) == 0:
                                # return 3m_stop
                                print(f'3m stop for {three_stop}mins and 6m stop for {six_stop}mins required')


