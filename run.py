import gspread
from google.oauth2.service_account import Credentials
import json


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

#print(data[0][1])
inputtedDepth = 50
inputtedMins = 126
three_stop = ""
six_stop = ""

if inputtedMins > 125:
    print("Not compatable")
else:
    for row in data:
        if row[0] != "meters":
            # print(int(row[0]))
            if inputtedDepth <= int(row[0]):
                # print(row[1])
                if inputtedMins <= int(row[1]):
                    # print(row[2])
                    if int(row[2]) == 0:
                        # return "No Deco Needed"
                        print("No Deco Needed")
                        break
                    else:
                        three_stop = row[2]
                    if int(row[3]) == 0:
                        # return 3m_stop
                        print(three_stop)
                        break
                    else:
                        six_stop = row[3]
                    if int(row[4]) == 0:
                        # return 3m_stop
                        print(f'3m stop for {three_stop}mins and 6m stop for {six_stop}mins required')


# with open('creds.json', 'r') as f:
#     table_dict = json.load(f)

# for table in table_dict:
#     print(table['meters'])

# def get_diver_inputs():
#     """
#     Requests diver to input their depth and time
#     """
#     print('Welcome to the Buehlmann Table for Air Diving Decompression')
#     print('Use this table to calculate your Repetitive Dive time and Residual Nitrogen Times\n')
#     start = input('Would you like to start a calculation y/n')
#     if start.lower() == 'y':
#         depth = input('Depth:')
#         time = input('Time:')

#         print(f"Depth of {depth} meters")
#         print(f"Time of {time} minutes")

#     elif start.lower() == 'n':
#         print('Exiting Calculator')
#     else:
#         print('That is not a valid input. Please try again')          


# get_diver_inputs()        








# """
# Calculates if you need a decompression stop
# """

# print('Your depth was {depth}')
# print('Your time was {time}')


# if input('Depth:') = 15 and input('Time:') >= 90:
#     print (deco)
