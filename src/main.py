'''
Created on Sep 20, 2017

@author: jlearx
'''

def getGameBoardSize():
    width = 0
    height = 0
    
    while ((width < 1) and (height < 1)): 
        inputStr = ""
        xPos = -1
        
        while (inputStr == ""):
            inputStr = input("Please enter the game board dimensions as wxh (eg. 3x3): ").strip()
            inputStr = inputStr.lower()
            
            if (len(inputStr) < 3):
                inputStr = ""                
                continue
            
            xPos = inputStr.find('x')
            
            if ((xPos < 1) or (xPos == len(inputStr) - 1)):
                inputStr = ""                
                continue
        
        width = int(inputStr[:xPos])
        height = int(inputStr[xPos + 1:])
        return (width,height)

def printRow(width):
    for i in range(0,width):
        print(" ---", end="")
        
    print(" ")
    
def printCol(width):
    for i in range(0,width):
        print("|   ", end="")
    
    print("|")

def printGameBoard(size):
    # size (x,y)
    width = size[0]
    height = size[1]
    
    for i in range(0,height):
        printRow(width)
        printCol(width)
    
    printRow(width)

if __name__ == '__main__':
    # size (x,y)
    size = getGameBoardSize()
    printGameBoard(size)
    