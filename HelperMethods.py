import gspread
from google.oauth2.service_account import Credentials
import json
import time
import getpass


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



class HelperMethods(object):

    data = Sheet1.get_all_values()

    def get_data(self):
        return self.data


    def info_on_tables(self):
        """
    #     Gives the user information on the functionality of the tables
    #     """
        print('''\nThe Bühlmann tables were created by Dr. Albert A. Bühlmann, a 
        swiss physician in 1983.''')
        time.sleep(1.5)
        print('''They display a mathematical algorithm which outlines the way in 
        which inert gases\n(specificlly nitrogen), enter and leave the body at 
        different ambient pressures.\n''')
        time.sleep(1.5)
        print('''Dive computers run off many algorithms, the Bühlmann algorithm 
        is one of these.''')
        time.sleep(1.5)
        print('''Recreational divers are not permitted to hit 'decos'\nor 
        decompression stops, during their dives.\n''')
        time.sleep(1.5)
        print('''Decompression stops are stops that a diver must do when surfacing,
        \nthey can be at 3m, 6m, 9m or deeper, 
        depending on the depth of dive.\n''')
        time.sleep(1.5)
        print('''These stops allow the divers body tissues time of 'off-gas'\nor 
        time for the nitrogen to leave the bodys cells.\n''')
        time.sleep(1.5)
        print('''Not allowing the body time to adequately off-gas can result 
        in\nan illness nown as decompression sickness or "the bends"s.\n''')
        time.sleep(1.5)
        print('''This is a condition that ranges from mild to life threatening\nand 
        involves nitrogen bubbles becoming too large in the divers blood\nand 
        blocking blood and, hence O2, from reaching divers tissues.\n''')
        time.sleep(1.5)
        print('''Using the Bühlmann tables or diving with a dive computer, we 
        can aim to\nmitigate these risks and enjoy the wonders of diving!\n''')
        time.sleep(1.5)
        print("Information complete")
        print("\n")
        input("To return home press enter\n")


    def dive_planning(self):
        """
        Function to allow user to plan their dives 
        based on max depth or max time
        """
        print('''\nYou can use this section to plan your dives 
        based on depths and times.\n''')
        time.sleep(2)
        print('''As recreational divers without extended range training,
        \nhitting a deco stop is not reccomended or covered by insurance\n''')
        print('''You can use this to calculate how long you can stay\nat your 
        desired depth for without hitting a deco,\nor how deep you can dive 
        for a set time without hitting a deco\n''')
        time.sleep(2)
        plan = input('''If you would like to find the max time for a given depth type
         "time"\nIf you would like to find the max depth for a given time
          type "depth"\nTo return to main menu type "home"\n''')

        if plan.lower() == 'time':
            print('''\nYou have selected to work out how long you can stay at a 
            given depth\n''')
            while True:
                try:
                    user_depth = int(input("Depth:\n"))
                    print("\n")
                    print(f"Depth of {user_depth} meters")
                    print("\n")
                    time.sleep(1.5)
                    break
                except ValueError:
                    print("\nPlease input a number only\n")
                    continue

            self.time_calculation(user_depth, self.data)

        elif plan.lower() == 'depth':
            print('''\nYou have selected to work out how deep you can go for a 
            given time\n''')
            while True:
                try:
                    user_time = int(input("Time:\n"))
                    print("\n")
                    print(f"Time of {user_time} minutes")
                    print("\n")
                    time.sleep(1.5)
                    break
                except ValueError:
                    print("Please input a number only")
                    continue
            self.depth_calculation(user_time, self.data)
        elif plan.lower() == "home":
            print("\n")
            time.sleep(1.5)
            print('\nYou have selcted to return to the main menu\n')
            time.sleep(2)
            print("\n")
            print("\nReturning to main menu\n")
            time.sleep(2)
            print(".")
            time.sleep(2)
            print(".")
            time.sleep(2)
            print("\n.\n")
        else:
            print('Invalid input')
            self.dive_planning()

    def time_calculation(self, user_depth, data):
        """
        Calculates time for a given depth
        """  
        longest_time = 0    
        larger_number_count = 0  
        assumed_depth = 0
        if int(user_depth) > 51:
            print('''Buehlmann tables do not support depths exceeding 51m, 
            please try again''')
        else:
            for row in data:
                if row[0] != "meters":
                    if int(user_depth) <= int(row[0]):
                        larger_number_count = larger_number_count+1
                        if larger_number_count == 1:
                            assumed_depth = int(row[0])
                        if assumed_depth == int(row[0]):
                            if int(row[2]) == 0:
                                longest_time = int(row[1])
            print("\n")   
            time.sleep(2)               
            print(f'Max time you can stay at this depth is: {longest_time} minutes')
            print("\n")
            time.sleep(2)
            input('\nTo return to main menu hit Enter\n')
            time.sleep(2)
            print("\n")
            print("\nReturning to main menu\n")
            time.sleep(2)
            print(".")
            time.sleep(2)
            print(".")
            time.sleep(2)
            print("\n.\n")


    def depth_calculation(self, user_time, data):
        """
        Calculates depth for a given time
        """
        deepest_depth = 0
        if int(user_time) > 125:
            print('''Buehlmann tables do not support dives exceeding 125 minutes, 
            please try again''')
        else:
            for row in data:
                if row[0] != "meters":
                    if int(user_time) <= int(row[1]):
                        if int(row[2]) == 0:
                            deepest_depth = int(row[0])
            print("\n")  
            time.sleep(2)    
            print("\n")          
            print(f"Deepest depth for {user_time} minutes is {deepest_depth} meters")
            print("\n")
            time.sleep(2)
            input('\nTo return to main menu hit Enter\n')
            time.sleep(2)
            print("\n")
            print("\nReturning to main menu\n")
            time.sleep(2)
            print(".")
            time.sleep(2)
            print(".")
            time.sleep(2)
            print("\n.\n")

