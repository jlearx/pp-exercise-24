'''
Created on Sep 20, 2017

@author: jlearx
'''

def getGameBoardSize():
    length = 0
    width = 0
    
    while ((length < 1) and (width < 1)): 
        inputStr = ""
        xPos = -1
        
        while (inputStr == ""):
            inputStr = input("Please enter the game board dimensions as lxw (eg. 3x3): ").strip()
            inputStr = inputStr.lower()
            
            if (len(inputStr) < 3):
                inputStr = ""                
                continue
            
            xPos = inputStr.find('x')
            
            if ((xPos < 1) or (xPos == len(inputStr) - 1)):
                inputStr = ""                
                continue
        
        length = int(inputStr[:xPos])
        width = int(inputStr[xPos + 1:])
        return (length,width)

if __name__ == '__main__':
    # (x,y)
    size = getGameBoardSize()
    print(str(size))
    