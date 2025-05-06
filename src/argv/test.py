import os.path
import sys

lineCounter = False
charCounter = False
wordCounter = False

def argsParce(args):
    i = 0
    fileName = ""
    arguments = ""
    for item in args:
        if i != 0:
            print(item)
        if i == 1:
            fileName = item
        if i >= 2:
            arguments += item
        i += 1

    if type(arguments) == list:
        for item in arguments:
            argConvert(item)
    else:
        argConvert(arguments)

    return fileName

def argConvert(item):
    global lineCounter, charCounter, wordCounter
    if item[0] == "-":
        for i in item[1:]:
            print(i)
            if i == "l":
                lineCounter = True
            if i == "c":
                charCounter = True
            if i == "w":
                wordCounter = True
    else:
        print(item)
        raise Exception("Аргументы отсутствуют")

def processFile(fileName):
    if os.path.isfile(fileName):
        with open(fileName) as file:
            file.readline()

def main():
    if len(sys.argv) > 2:
        fileName = argsParce(sys.argv)
        processFile(fileName)
    else:
        raise Exception("Недостаточно аргументов")

    print(lineCounter)

if __name__ == "__main__":
    main()