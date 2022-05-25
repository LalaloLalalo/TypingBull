from typing import KeysView
from cmu_graphics import * 
import time

app.stepsPerSecond = 60
app.background = 'pink'

Timer = Label('0', 30,25, fill = 'white', size = 40)
startTime = time.time()
Timer.stopped = False 
wpm = Label('0', 360,25, fill = 'white', size = 40)
ground = Group(
    
    Rect(-10,220,420,200, fill = 'black', border = 'white', borderWidth = 5)

)

import os
thisFolder = os.path.dirname(os.path.realpath(__file__))

leftB = Image(thisFolder + '/bullleft.png', 255,155, height = 80, width = 110)

rightB = Image(thisFolder + '/bullright.png',55,155, height = 80, width = 110)

pointer = Group(

    Line(50,254,50, 274, fill = 'White' ) 

)
leftB.rotateAngle = -5
rightB.rotateAngle = 5
lables = Group
app.engwords = ['from', 
            'about','their', 'will', 'would',
            'make', 'just', 'think', 'time',
            'take', 'year', 'them',
            'want', 'when', 'which',
            'like', 'other', 'could',
            'into','here', 'then', 'than', 'look',
            'more', 'these', 'thing', 'well', 
            'also','good',
            'first', 'find', 'give',
            'need', 'back', 'even']


app.rows = 4
app.cols = 5

app.gameWords = makeList(app.rows, app.cols)

app.rowIndex = 0
app.colIndex = 0
app.charIndex = 0

app.match = makeList(app.rows,app.cols)

def Random():
    for row in range(app.rows):
        for col in range(app.cols):
            centerX = 56 + col * 65
            centerY = 270 + row * 30
            randomword = choice(app.engwords)
            app.gameWords[row][col] = randomword
            wordGraphic = []
            for i in range(len(randomword)):
                wordGraphic.append(Label(randomword[i], centerX + 10 * i, centerY, fill = 'white', size = 18, align = 'bottom', font = 'caveat' ))

            app.match[row][col] = wordGraphic

Random()


def onStep():
    rightB.centerX += 1
    if(Timer.stopped == False):
        Timer.value = rounded(time.time()-startTime)
    if(rightB.right - 5 >= leftB.left + 5):
        depth = (rightB.right - 5) - (leftB.left + 5)
        rightB.right -= depth/2
        leftB.left += depth/2
    if(rightB.right <= 0 ):
        Timer.stopped = True
    if(leftB.left >= 400):
        Timer.stopped = True
        
        
    

    

def onKeyPress(key):
    if('space' == key):
        app.charIndex = 0
        app.colIndex += 1

        if(app.colIndex > app.cols - 1):

            if(app.rowIndex == app.rows - 1):
                Rect(-10,220,420,200, fill = 'black', border = 'white', borderWidth = 5)
                Random()
                app.rowIndex = 0
                app.colIndex = 0
                pointer.toFront()
                return
            
            app.rowIndex += 1
            app.colIndex = 0

        pointer.centerX = app.match[app.rowIndex][app.colIndex][app.charIndex].centerX - app.match[app.rowIndex][app.colIndex][app.charIndex].width/2
        pointer.centerY = app.match[app.rowIndex][app.colIndex][app.charIndex].centerY
        return

    
    if('backspace' == key):
        if(not(app.charIndex == 0 and app.colIndex == 0 and app.rowIndex == 0)):

            app.charIndex -= 1
            pointer.centerX = app.match[app.rowIndex][app.colIndex][app.charIndex].centerX - app.match[app.rowIndex][app.colIndex][app.charIndex].width/2
            pointer.centerY = app.match[app.rowIndex][app.colIndex][app.charIndex].centerY
            app.match[app.rowIndex][app.colIndex][app.charIndex].fill = 'white'
            if(app.charIndex < 0):
                app.colIndex -= 1
                pointer.centerX = app.match[app.rowIndex][app.colIndex][app.charIndex].centerX - app.match[app.rowIndex][app.colIndex][app.charIndex].width/2
                pointer.centerY = app.match[app.rowIndex][app.colIndex][app.charIndex].centerY
                if(app.colIndex < 0):
                    app.rowIndex -= 1
                    pointer.centerX = app.match[app.rowIndex][app.colIndex][app.charIndex].centerX - app.match[app.rowIndex][app.colIndex][app.charIndex].width/2
                    pointer.centerY = app.match[app.rowIndex][app.colIndex][app.charIndex].centerY
                    app.colIndex = app.cols - 1
                app.charIndex = len(app.gameWords[app.rowIndex][app.colIndex]) - 1
                app.match[app.rowIndex][app.colIndex][app.charIndex].fill = 'white'
                


        return

        

    if(app.rowIndex < app.rows):
        if(app.colIndex < app.cols):
            if(app.charIndex < len(app.gameWords[app.rowIndex][app.colIndex])):
                if(app.gameWords[app.rowIndex][app.colIndex][app.charIndex] == key):
                    app.match[app.rowIndex][app.colIndex][app.charIndex].fill = 'limeGreen'
                    leftB.centerX -=10
                else:
                    app.match[app.rowIndex][app.colIndex][app.charIndex].fill = 'red'
                    leftB.centerX += 5
                pointer.centerX = app.match[app.rowIndex][app.colIndex][app.charIndex].centerX + app.match[app.rowIndex][app.colIndex][app.charIndex].width/2
                pointer.centerY = app.match[app.rowIndex][app.colIndex][app.charIndex].centerY
 
                app.charIndex += 1                 

        else:
            app.rowIndex += 1
            app.colIndex = 0
   

    

    if('tab' in key):
        app.reload()

    #if('enter' in key):
       # app.paused = False



    
    



cmu_graphics.run()
