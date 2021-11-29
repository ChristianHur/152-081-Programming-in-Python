"""
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
"""

# Minute constants
ONE = "one"
TWO = "two"
THREE = "three"
FOUR = "four"
FIVE = "five"
SIX = "six"
SEVEN = "seven"
EIGHT = "eight"
NINE = "nine"

TEN = "ten"
TWENTY = "twenty"
THIRTY = "thirty"
FORTY = "forty"
FIFTY = "fifty"

ELEVEN = "eleven"
TWELVE = "twelve"
THIRTEEN = "thirteen"
FOURTEEN = "fourteen"
FIFTEEN = "fifteen"
SIXTEEN = "sixteen"
SEVENTEEN = "seventeen"
EIGHTTEEN = "eightteen"
NINETEEN = "nineteen"

# Get the English time name in a point in time
def getTimeName(hours, minutes, period):
    
    timeName = None
    pastTheHour = ''
    
    if minutes == '45':
    
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
        
    elif minutes == '0':
        timeName = str(hours) + " o'clock " + period
    elif minutes == '15':
        timeName = "a quarter after " + str(hours) + ' ' + period
    elif minutes == '30':
        timeName = "half past " + str(hours) + ' ' + period
    else:
        pastTheHour = " minutes past " + str(hours) + ' ' + period
        
        # Set time name for minutes between 1 and 19
        if minutes == '1': timeName = ONE
        if minutes == '2': timeName = TWO
        if minutes == '3': timeName = THREE
        if minutes == '4': timeName = FOUR
        if minutes == '5': timeName = FIVE
        if minutes == '6': timeName = SIX
        if minutes == '7': timeName = SEVEN
        if minutes == '8': timeName = EIGHT
        if minutes == '9': timeName = NINE
        if minutes == '10': timeName = TEN
        if minutes == '11': timeName = ELEVEN
        if minutes == '12': timeName = TWELVE
        if minutes == '13': timeName = THIRTEEN
        if minutes == '14': timeName = FOURTEEN
        if minutes == '16': timeName = SIXTEEN
        if minutes == '17': timeName = SEVENTEEN
        if minutes == '18': timeName = EIGHTTEEN
        if minutes == '19': timeName = NINETEEN       
        
        # Minutes name for twenties, thirties, forties, and fifties
        if minutes >= '20': 
            timeName = getMinutesName(minutes)            
        
    return timeName + pastTheHour

# Get the English minute name
def getMinutesName(minutes):   
    if minutes[0] == '2': timeName = TWENTY
    elif minutes[0] == '3': timeName = THIRTY
    elif minutes[0] == '4': timeName = FORTY
    else : timeName = FIFTY

    if minutes[1] == '1': return timeName + '-' + ONE
    if minutes[1] == '2': return timeName + '-' + TWO
    if minutes[1] == '3': return timeName + '-' + THREE
    if minutes[1] == '4': return timeName + '-' + FOUR
    if minutes[1] == '5': return timeName + '-' + FIVE
    if minutes[1] == '6': return timeName + '-' + SIX 
    if minutes[1] == '7': return timeName + '-' + SEVEN
    if minutes[1] == '8': return timeName + '-' + EIGHT
    if minutes[1] == '9': return timeName + '-' + NINE 
    return ''

# Read the hours, minutes, and period from user
def getTime():
    hours = int(input("Enter the hours (1-12):"))
    minutes = input("Enter minutes (0-59):")
    period= input("Enter period (AM/PM):").upper()
    return hours,minutes,period    

# Main entry to program
def main():
    hours,minutes,period = getTime()
    if hours > 12 or hours < 0 or int(minutes) > 59 or int(minutes) < 0 or period != 'AM' and period != 'PM':
        print("*** Error:  Sorry, invalid time. Good-bye. ***")
    else:
        timeName = getTimeName(hours,minutes,period)
        print("The time is",timeName + '.')
        
main()
