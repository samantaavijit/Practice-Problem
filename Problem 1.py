"""
19/Sep/2020
Your age in 2090
Take age or year of birth input from the user and tell them when will they return 100 years old
They can then optionally provide a year and your program must tell their age in that particular year.

You should be handling all sorts of error like:
      1) You are not yet born if year of birth > 2020 or age==0
      2) You seem to the oldest person alive if year of birth <1895
      3) You can also handle any other error if possible
"""
import datetime

if __name__ == '__main__':
    try:
        age = int(input("Please enter your age or Year of birth "))
        year = int(input("Please enter the year that will show your age of this particular year "))
        current_year = datetime.datetime.now().year
        if age <= 0 or year <= 0:
            print("You are not yet born")
            exit()
        if age > 1890:  # It is year because it > 1890
            if age > current_year:
                print("You are not yet born")
            else:
                current_age = current_year - age
                if year < 1890:  # suppose it is after 100 years not after 2050
                    print(f"Your age is {current_age + year} after {current_year + year} year's ago")
                else:
                    if year < age:  # age is 1999 but year is 1900
                        print(
                            f"You enter wrong input your age now {current_age} in {current_year} but you see after {year} "
                            f"this year. Time travel is not possible :> :>")
                    elif year < current_year:  # 2010<2020 i already know my age in 2010
                        print(f"You already know your age in {year} is {(year - age)} :) :)")
                    elif year == current_year:
                        print(f"You are {current_age} year's old")
                    elif year > current_year + 130:
                        print(f"You seem to the oldest person alive and age is {(year - age)}")
                    else:
                        print(f"In {year} your age will be {(year - age)}")
        else:
            if year < 1890:
                print(f"Your age is {age + year} after {current_year + year} year's ago")
            else:
                if year < current_year:  # 2010 <2020
                    print(f"You already know your age in {year} is {(age - (current_year - year))} :) :)")
                elif year == current_year:
                    print(f"You are {age} year's old")
                else:
                    print(f"In {year} your age will be {age + (year - current_year)}")
    except ValueError:
        print("Enter valid input")
    except Exception as e:
        print(e)
