import gspread
from google.oauth2.service_account import Credentials

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

print(data)


# print('Welcome to the Buehlmann Table for Air Diving Decompression')
# print('Use this table to calculate your Repetitive Dive time and Residual Nitrogen Times')




# continue_calculation = input('Would you like to start a calculation y/n')

# if continue_calculation.lower() == 'y':
#     depth = input('Depth:')
#     time = input('Time:')

# elif continue_calculation.lower() == 'n':
#     print('Exiting Calculator')
   
# else:
#     print('That is not a valid input. Please try again')  




# """
# Calculates if you need a decompression stop
# """

# print('Your depth was {depth}')
# print('Your time was {time}')


# if input('Depth:') = 15 and input('Time:') >= 90:
#     print (deco)
