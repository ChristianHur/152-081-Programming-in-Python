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

Write a program that reads a file containing text. Read each line and send it to the output file, in reverse order. If the input file contains:
Mary had a little lamb
Whose fleece was white as snow. 
And everywhere that Mary went,
The lamb was sure to go!
then the program produces the output file
The lamb was sure to go!
Mary had a little lamb
Whose fleece was white as snow.
And everywhere that Mary went,

Also, print the number of characters (exclude white spaces), words, and lines in the input file.  We will consider a word is one or more characters surrounded by white spaces.  For example, the sample input file above should print:
Character count: 89 
Word count:  22
Line count: 4
'''

def main():
    infile = open("littlelamb.txt","r")
    lines = infile.readlines()
    print("\n")
    printLines(lines)
    print("\n")
    charCount = getCharCount(lines)
    wordCount = getWordCount(lines)
    lineCount = getLineCount(lines)
    printResult(charCount, wordCount, lineCount)

def printResult(charCount, wordCount, lineCount):
    print("Character count:",charCount)
    print("Word count:",wordCount)
    print("Line count:",lineCount)

def printLines(lines):
    for i in range(len(lines)-1,-1,-1):
        print(lines[i].rstrip("\n").strip(" "))
    
def getCharCount(lines):
    count = 0
    for line in lines:
        for char in line:
            if char.strip() != "":
                count += 1
    return count

def getWordCount(lines):
    count = 0
    for line in lines:
        words = line.split(" ")
        count += len(words)
    return count

def getLineCount(lines):
    return len(lines)


main()