def main():
    IO_Error = False
    try:
        infile = open("littlelamb.txt","r")
    except:
        IO_Error = True
        print("*** ERROR:  Could not open file. ***")

    if not IO_Error:
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
