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
        