# ask user to input year they'd like to check
year = int(input("Which year do you want to check? "))

# function to check if a year is a leap year
def leapyear(year):
    # if year divisible by 4
    if year % 4 == 0:
        # and divisible by 100
        if year % 100 != 0:
            # then it's a leap year
            print('Leap year.')
        # or divisible by hundred and four hundred
        elif year % 100 == 0 and year % 400 == 0:
            # then it's a leap year
            print('Leap year.')
        else:
            # else, not a leap year
            print('Not leap year.')
    
    # if year not divisible by 4
    else:
        # then it's not a leap year
        print('Not leap year.')

leapyear(year)