print('Welcome to the Buehlmann Table for Air Diving Decompression')
print('Use this table to calculate your Repetitive Dive time and Residual Nitrogen Times')

calculating = True

while calculating:
    continue_calculaton = input('Would you like to start a calculation y/n')
    if continue_calculation.lower() == 'y':
        print('Input your depth and time below')
    elif continue_calculation.lower() == 'n':
        print('Exiting Calculator')
        calculating = False
    else:
        print('That is not a valid input. Please try again')  

print('Thanks for using the Dive Table Calculator')
