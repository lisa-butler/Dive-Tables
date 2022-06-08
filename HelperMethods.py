import gspread
from google.oauth2.service_account import Credentials
import json
import time
import getpass
import os

class HelperMethods(object):


    def info_on_tables(self):
        """
    #     Gives the user information on the functionality of the tables
    #     """
        print("\nThe Bühlmann tables were created by Dr. Albert A. Bühlmann, a swiss physician in 1983.")
        time.sleep(1.5)
        print("They display a mathematical algorithm which outlines the way in which inert gases\n(specificlly nitrogen), enter and leave the body at different ambient pressures.\n")
        time.sleep(1.5)
        print("Dive computers run off many algorithms, the Bühlmann algorithm is one of these.")
        time.sleep(1.5)
        print("Recreational divers are not permitted to hit 'decos'\nor decompression stops, during their dives.\n")
        time.sleep(1.5)
        print("Decompression stops are stops that a diver must do when surfacing,\nthey can be at 3m, 6m, 9m or deeper, depending on the depth of dive.\n")
        time.sleep(1.5)
        print("These stops allow the divers body tissues time of 'off-gas'\nor time for the nitrogen to leave the bodys cells.\n")
        time.sleep(1.5)
        print("Not allowing the body time to adequately off-gas can result in\nan illness nown as decompression sickness or 'the bends.\n")
        time.sleep(1.5)
        print("This is a condition that ranges from mild to life threatening\nand involves nitrogen bubbles becoming too large in the divers blood\nand blocking blood and, hence O2, from reaching divers tissues.\n")
        time.sleep(1.5)
        print("Using the Bühlmann tables or diving with a dive computer, we can aim to\nmitigate these risks and enjoy the wonders of diving!\n")
        time.sleep(1.5)
        print("Information complete")
        print("\n")
        input("To return home press enter\n")


    def dive_planning(self):
        """
        Function to allow user to plan their dives based on max depth or max time
        """
        print("\nYou can use this section to plan your dives based on depths and times.\n")
        time.sleep(2)
        print("As recreational divers without extended range training,\nhitting a deco stop is not reccomended or covered by insurance\n")
        print("You can use this to calculate how long you can stay\nat your desired depth for without hitting a deco,\nor how deep you can dive for a set time without hitting a deco\n")
        time.sleep(2)
        plan = input("If you would like to find the max time for a given depth type 'time'\nIf you would like to find the max depth for a given time type 'depth'\nTo exit type 'exit'\n")

    #     if plan.lower() == 'time':
    #         print('You have selected to work out how long you can stay at a given depth\n')
    #         user_depth = input('Please type depth')
    #         print(f'You have input a depth of {user_depth} meters')
    #         time_calculation()

    #     elif plan.lower() == 'depth':
    #         print('You have selected to work out how deep you can go for a given time\n')
    #         user_time = input('Please type time')
    #         print(f'You have input a time of {user_time} minutes')
    #         depth_calculation()


    # def time_calculation():
    #     """
    #     Calculates time for a given depth
    #     """        
    #     if int(user_depth) > 51:
    #         print("Buehlmann tables do not support depths exceeding 51m, please try again")
    #     else:
    #         for row in data:
    #             # column 0 find depth, for this depth find highest time with no deco
    #             if (user_depth) <= int(row[0]):
    #                 if int(row[2]) == 0:
    #                     # if int(row[1]) higest value in that section


    # def depth_calculation():
    #     """
    #     Calculates depth for a given time
    #     """
    #     if int(user_time) > 125:
    #         print("Buehlmann tables do not support dives exceeding 125 minutes, please try again")
    #     else:
    #         for row in data:
    #             if (user_time) <= int(row[1]):
    #                 if int(row[2]) == 0:
                        # if find maximum dpeth for this time 