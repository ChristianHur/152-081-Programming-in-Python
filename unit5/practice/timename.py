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

Write a function get_time_name(hours, minutes, period) that returns the English
name for a point in time.  If the minutes are exactly 15, 30, or 45, the it
should read "a quarter after ... or a quarter to ..., half past ...".  If the
minutes is 0 then it should read "... o'clock".  Assume that hours is
between 1 and 12.

Examples:

get_time_name(8,0,AM)                # 8 o'clock am
get_time_name(8,15,PM)               # a quarter after 8 pm
get_time_name(8,30,AM)               # half past 8 am
get_time_name(8,45,PM)               # a quater to 9 am
get_time_name(8,12,AM)               # twelve minutes past 8 am
'''

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
def get_time_name(hours, minutes, period):
    
    time_name = None
    past_the_hour = ''
    
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
        
        time_name = "a quarter to " + str(hours) + ' ' + period
        
    elif minutes == '0':
        time_name = str(hours) + " o'clock " + period
    elif minutes == '15':
        time_name = "a quarter after " + str(hours) + ' ' + period
    elif minutes == '30':
        time_name = "half past " + str(hours) + ' ' + period
    else:
        past_the_hour = " minutes past " + str(hours) + ' ' + period
        
        # Set time name for minutes between 1 and 19
        if minutes == '1': time_name = ONE
        if minutes == '2': time_name = TWO
        if minutes == '3': time_name = THREE
        if minutes == '4': time_name = FOUR
        if minutes == '5': time_name = FIVE
        if minutes == '6': time_name = SIX
        if minutes == '7': time_name = SEVEN
        if minutes == '8': time_name = EIGHT
        if minutes == '9': time_name = NINE
        if minutes == '10': time_name = TEN
        if minutes == '11': time_name = ELEVEN
        if minutes == '12': time_name = TWELVE
        if minutes == '13': time_name = THIRTEEN
        if minutes == '14': time_name = FOURTEEN
        if minutes == '16': time_name = SIXTEEN
        if minutes == '17': time_name = SEVENTEEN
        if minutes == '18': time_name = EIGHTTEEN
        if minutes == '19': time_name = NINETEEN       
        
        # Minutes name for twenties, thirties, forties, and fifties
        if minutes >= '20': 
            time_name = get_minutes_name(minutes)            
        
    return time_name + past_the_hour

# Get the English minute name
def get_minutes_name(minutes):   
    if minutes[0] == '2': time_name = TWENTY
    elif minutes[0] == '3': time_name = THIRTY
    elif minutes[0] == '4': time_name = FORTY
    else : time_name = FIFTY

    if minutes[1] == '1': return time_name + '-' + ONE
    if minutes[1] == '2': return time_name + '-' + TWO
    if minutes[1] == '3': return time_name + '-' + THREE
    if minutes[1] == '4': return time_name + '-' + FOUR
    if minutes[1] == '5': return time_name + '-' + FIVE
    if minutes[1] == '6': return time_name + '-' + SIX 
    if minutes[1] == '7': return time_name + '-' + SEVEN
    if minutes[1] == '8': return time_name + '-' + EIGHT
    if minutes[1] == '9': return time_name + '-' + NINE 
    return ''

# Read the hours, minutes, and period from user
def get_time():
    hours = int(input("Enter the hours (1-12):"))
    minutes = input("Enter minutes (0-59):")
    period= input("Enter period (AM/PM):").upper()
    return hours, minutes, period    

# Main entry to program
def main():
    hours, minutes, period = get_time()
    if hours > 12 or hours < 0 or int(minutes) > 59 or int(minutes) < 0 or period != 'AM' and period != 'PM':
        print("*** Error:  Sorry, invalid time. Good-bye. ***")
    else:
        time_name = get_time_name(hours, minutes, period)
        print("\nThe time is", time_name + '.')
        
main()
