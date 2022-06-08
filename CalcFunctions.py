import json
from HelperMethods import HelperMethods

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


