def print_leap_year(year):
    if(year % 4==0):
        print(year, "is a leap year")
    else:
        print(input(" enter the  year"))
year=int(input ("enter the year"))
print_leap_year(year)  