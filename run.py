print('Welcome to the Buehlmann Table for Air Diving Decompression')
print('Use this table to calculate your Repetitive Dive time and Residual Nitrogen Times')




continue_calculation = input('Would you like to start a calculation y/n')

if continue_calculation.lower() == 'y':
    depth = input('Depth:')
    time = input('Time:')

elif continue_calculation.lower() == 'n':
    print('Exiting Calculator')
   
else:
    print('That is not a valid input. Please try again')  




"""
Calculates if you need a decompression stop
"""

print('Your depth was {depth}')
print('Your time was {time}')


# if input('Depth:') = 15 and input('Time:') >= 90:
#     print (deco)
