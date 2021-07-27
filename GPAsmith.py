# This program allows a user to input their name, credit hours, and quality points. Then it calculates their GPA and outputs their name and GPA.
import time

name = str(input('What is your name? ')) # asks user for their name

hours = int(input('How many credit hours have you earned? ')) # asks user for credit hours earned

points = int(input('How many quality points do you have? ')) # asks user for amount of quality points

gpa = points / hours  # calculates GPA
gpa = round(gpa, 2)  #rounds gpa 2 decimal places

print ('Hi ' + str(name) + '. ' + 'Your grade point average is ' + str(gpa) + '.') # displays users name and GPA

time.sleep(5)
