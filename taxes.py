#Name: Pierce Arnold

import datetime

TAX_RATE = 0.044
RELIEF_RATE = 0.3

#define global variables
relief = 1
value = 0
annual_cost = 0
six_month_cost = 0
relief_amount = 0
total = 0



############# define program functions #############
def main():

    more = True
    while more:
            get_user_data()
            perform_calculations()
            display_results()

            yesno = input("\nWould you like to calculate tax for another vehicle? (Y/N): ")
            if yesno == "n" or yesno == "N":
                more = False
                print("Personal Property tax due JUNE 05")

def get_user_data():
    global relief, value
    print("**** PERSONAL PROPERTY TAX BILL ****")
    value = int(input("Assesed value of the vehicle: $ "))
    relief = int(input("\nIs your vehicle eligible for tax relief? (1 for YES, 2 for NO): "))

def perform_calculations():
    global TAX_RATE, RELIEF_RATE, relief, vlaue, annual_cost, six_month_cost, total, relief_amount

    annual_cost = value * TAX_RATE
    six_month_cost = annual_cost * 0.5

    if relief == 1:
        relief_amount = six_month_cost * RELIEF_RATE
    else:
        relief_amount = 0
        
    total = six_month_cost - relief_amount


    #NOTE: This program does not provide the same numbers for relief amount and full annual amount as the example in the google doc
    # despite giving the same total due as the example in the google doc. I could not find any issue
    # in my program and my numbers match with the image provided of the real life bill. I also noticed
    # that the google doc uses the value of 30% relief at one point and 33% at another point; I used
    # the 30% because it led to my results matching the provided numbers. The last thing is that I
    # found is that the next section on taxes using lists uses the 33% number and uses 4.2% for the
    # tax rate per year in contrast to the 4.4% used in this section.

def display_results():
    currency = '8,.2f'
    line = '----------------------------------------'

    print(line)
    print('**** PERSONAL PROPERTY TAX BILL ****')
    print('    Please Pay in a Timely Manner')
    print("        Date/Time: " + str(datetime.datetime.now()))
    print(line)
    print('        Assessed Value        $ ' + format(value,currency))
    print('        Relief Amount         $ ' + format(relief_amount,currency))
    print('        Full Annual Amount    $ ' + format(annual_cost,currency))
    print(line)
    print('        Total Due             $ ' + format(total,currency))



main()
