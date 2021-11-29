'''
MIT License

Copyright (c) 2021 Christian Hur (Gateway Technical College)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

------------
Description:
------------

Write a function getTimeName(hours, minutes, period) that returns the English name for a point in time.  If the minutes are exactly 15, 30, or 45, the it should read "a quarter after ... or a quarter to ..., half past ...".  If the minutes is 0 then it should read "... o'clock".  Assume that hours is between 1 and 12.

Examples:

getTimeName(8,0,AM)                 # 8 o'clock am
getTimeName(8,15,PM)               # a quarter after 8 pm
getTimeName(8,30,AM)               # half past 8 am
getTimeName(8,45,PM)               # a quater to 9 am
getTimeName(8,12,AM)               # twelve minutes past 8 am
'''

# Constants
MINUTES = ["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
T10 =  ["ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eightteen", "nineteen"]
T2050 = ["","", "twenty", "thirty", "forty", "fifty"]

# Get the English time name in a point in time
def getTimeName(hours, minutes, period):

    timeName = None
    pastTheHour = ''

    if minutes == 45:

        # Set the correct period
        if hours == 11:
            if period =='AM':
                period = 'PM'
            else:
                period = 'AM'

        # Set the correct hour when hour is 12
        if hours == 12:
            hours = 1
        else:
            hours += 1

        timeName = "a quarter to " + str(hours) + ' ' + period

    elif minutes == 0:
        timeName = str(hours) + " o'clock " + period
    elif minutes == 15:
        timeName = "a quarter after " + str(hours) + ' ' + period
    elif minutes == 30:
        timeName = "half past " + str(hours) + ' ' + period
    else:
        timeName = getMinutesName(minutes)
        minute_text = "minutes" if minutes > 1 else "minute"
        pastTheHour = ' ' + minute_text + " past " + str(hours) + ' ' + period

    return timeName + pastTheHour

# Get the English minute name1
def getMinutesName(minutes):
    m = int(minutes/10) # the first digit
    n = minutes % 10    # the second digit
    
    if minutes < 10:
        minutes_word = MINUTES[minutes]
    elif minutes < 20:
        minutes_word = T10[n]
    else:
        minutes_word = T2050[m]
        minutes_word += '' if n == 0 else '-' + MINUTES[n]
    return minutes_word


# Read the hours, minutes, and period from user
def getTime():
    hours = int(input("Enter the hours (1-12):"))
    minutes = int(input("Enter minutes (0-59):"))
    period= input("Enter period (AM/PM):").upper()
    return hours, minutes, period


# Main entry to program
def main():
    hours, minutes, period = getTime()

    if hours > 12 or hours < 0 or minutes > 59 or minutes < 0 or period != 'AM' and period != 'PM':
        print("*** Error:  Sorry, invalid time. Good-bye. ***")
    else:
        timeName = getTimeName(hours, minutes, period)
        print("\nThe time is", timeName + '.')

main()
