import gspread
from google.oauth2.service_account import Credentials
import json
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


# #print(data[0][1])
# inputtedDepth = 0
# inputtedMins = 0
# three_stop = ""
# six_stop = ""

def landing_page():
    """
    First page user encounters before entering program
    """
    print("Buehlmann Table for Air Diving Decompression /n")
    user_name = input("Please enter you name \n")
    print(f"Welcome {user_name}")
    enter_page = input("Press any key to start")

# main_menu():


def info_on_tables():
    """
    Gives the user information on the functionality of the tables
    """
    print("The Bühlmann tables were created by Dr. Albert A. Bühlmann, a swiss physician in 1983")
    time.sleep(1)
    print("They display a mathematical algorithm which outlines the way in which inert gases (specificlly nitrogen), enter and leave the body at different ambient pressures\n")
    print("Dive computers run off many algorithms, the Bühlmann algorithm is one of these")
    print("Recreational divers are not permitted to hit 'decos' or decompression stops, during their dives\n")
    print("Decompression stops are stops that a diver must do when surfacing, they can be at 3m, 6m, 9m or deeper, depending on the depth of dive\n")
    print("These stops allow the divers body tissues time of 'off-gas' or time for the nitrogen to leave the bodys cells\n")
    print("Not allowing the body to adequately off-gas can result in an illness nown as decompression sickness or 'the bends\n")
    print("This is a condition that ranges from mild to life threatening and involves nitrogen bubbles becoming too large in the divers blood and blocking blood and, hence O2, from reaching divers tissues\n")
    print("Using the Bühlmann tables or diving with a dive computer, we can aim to mitigate these risks and enjoy the wonders of diving!\n")
    print("Information complete")
    print("\n")

    exit_info = input('Press any key to return home')


# main_menu():


def main_menu():
    """
    Runs main welcome message and optional branches
    """
    print('Welcome to the Buehlmann Table for Air Diving Decompression\n')
    time.sleep(1)
    print('This calculator will provide you with the means to calculate your decompression times or plan a dive\n')
    time.sleep(1)
    print('You can also access information about the Buehlmann Table and why it was created\n')
    time.sleep(1)
    print('Would you like to read some information about dive tables? Make a dive plan? Or calculate your deco stops?\n')
    time.sleep(1)
    options_main = input('For information type "info", for dive planning type "plan" and for deco stop calculation type "deco"\n')
    while main_menu:
        if options_main.lower() == "info":
            print("You have selected to view the information page")
            print("\n")
            info_on_tables()
            break
        elif options_main.lower() == "plan":
            print("You have selected to visit the dive planning page")
            # dive_plannig_main()
        elif options_main.lower() == "deco":
            print("You have selected to visit the deco stop calculation page")
            print("\n")
            # deco_calculator()
        else:
            if options_main.lower() != "info" or "plan" or "deco":
                print("Invalid input, please try again")
                print("\n")
                main_menu()
                break
                



main_menu()


# def deco_calculator():
#     """
#     Requests diver to input their depth and time
#     """

#     print('You have selected to calculate if a decompression stop is needed for a given depth and time\n')
#     start = input('Would you like to start a calculation y/n')
#     if start.lower() == 'y':
#         inputtedDepth = input('Depth:')
#         inputtedMins = input('Time:')

#         print(f"Depth of {inputtedDepth} meters")
        # print(f"Time of {inputtedMins} minutes")

#         return [inputtedDepth, inputtedMins]


# res = deco_calculator()()
# inputtedDepth = res[0]
# inputtedMins = res[1]

# print(f"Your dive was {inputtedDepth} meters for {inputtedMins} minutes ")

# if int(inputtedMins) > 125 or int(inputtedDepth) > 51:
#     print("Buehlmann tables do not support depths exceeding 51m and dives exceeding 125 minutes, please try again")
# else:
#     for row in data:
#         if row[0] != "meters":
#             # print(int(row[0]))
#             if int(inputtedDepth) <= int(row[0]):
#                 # print(row[1])
#                 if int(inputtedMins) <= int(row[1]):
#                     # print(row[2])
#                     if int(row[2]) == 0:
#                         # return "No Deco Needed"
#                         print("No decompression stop needed")
#                         break
#                     else:
#                         three_stop = row[2]
#                     if int(row[3]) == 0:
#                         # return 3m_stop
#                         print(three_stop)
#                         break
#                     else:
#                         six_stop = row[3]
#                     if int(row[4]) == 0:
#                         # return 3m_stop
#                         print(f'3m stop for {three_stop}mins and 6m stop for {six_stop}mins required')



# def dive_planning_main():
#     """
#     Function to allow user to plan their dives based on max depth or max time
#     """
#     print("You can use this section to plan your dives based on depths and times\n")
#     print("As recreational divers without extended range training, hitting a deco stop is not reccomended or covered by insurance\n")
#     print("You can use this to calculate how long you can stay at your desired depth for without hitting a deco, or how deep you can dive for a set time without hitting a deco\n")
#     plan = input("If you would like to find the max time for a given depth type 'time' if you would like to find the max depth for a given time type 'depth'\n")

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
#                     # if find maximum dpeth for this time 