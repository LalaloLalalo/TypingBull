from colorsys import ONE_THIRD
from turtle import Turtle
from typing import KeysView
from cmu_graphics import * 
import time

app.stepsPerSecond = 60
app.background = 'darkSlateGrey'

Timer = Label('0', 30,25, fill = 'white', size = 40)
startTime = time.time()
Timer.stopped = False 
wpm = Label('0', 360,25, fill = 'white', size = 40)
wpmText = Label('WPM:', 300, 25, fill = 'white', size = 20 )
ground = Group(
    
    Rect(-10,220,420,200, fill = 'black', border = 'white', borderWidth = 5)

)

import os
thisFolder = os.path.dirname(os.path.realpath(__file__))

leftB = Image(thisFolder + '/bullleft.png', 255,152, height = 90, width = 120)

#leftB2 = Image(thisFolder + '/bullleft2.png', 255,155, height = 90, width = 120)

#leftB3 = Image(thisFolder + '/bullleft3.png', 255,155, height = 90, width = 120)

rightB = Image(thisFolder + '/bullright1.png',55,139, height = 90, width = 120)

rightB2 = Image(thisFolder + '/bullright3.png', 55,139, height = 90, width = 120)

rightB3 = Image(thisFolder + '/bullright2.png', 55,139, height = 90, width = 120)

rightB4 = Image(thisFolder + '/bullright2.png', 55,139, height = 90, width = 120)

rightB.visible = True
rightB2.visible = False
rightB3.visible = False
rightB4.visible = False


rightBSpeed = 0.35
pointer = Group(

    Line(50,254,50, 274, fill = 'White' ) 

)
leftB.rotateAngle = -5
rightB.rotateAngle = 5
rightB2.rotateAngle = 5
rightB3.rotateAngle = 5
rightB4.rotateAngle = 5
lables = Group
app.counter = 0
betweenCount = 5
app.engwords = ['from', 
            'about','their', 'will', 'would','make', 'child', 
            'make', 'just', 'think', 'time','another',
            'take', 'year', 'them','still','come',
            'want', 'when', 'which',
            'like', 'other', 'could',
            'into','here', 'then', 'than', 'look',
            'more', 'these', 'thing', 'well', 
            'also','good','system','large',
            'first', 'find', 'give',
            'need', 'back', 'even','nation','while',]


app.rows = 4
app.cols = 5

app.gameWords = makeList(app.rows, app.cols)

app.rowIndex = 0
app.colIndex = 0
app.charIndex = 0
prevX = 0
app.match = makeList(app.rows,app.cols)

def Random():
    for row in range(app.rows):
        for col in range(app.cols):
            centerX = 61 + col * 65
            if(col != 0):
                centerX = 20 + app.match[row][col - 1][len(app.match[row][col - 1]) - 1].centerX
            centerY = 270 + row * 30
            randomword = choice(app.engwords)
            app.gameWords[row][col] = randomword
            wordGraphic = []
            for i in range(len(randomword)):
                wordGraphic.append(Label(randomword[i], centerX + 10 * i, centerY, fill = 'white', size = 18, align = 'bottom', font = 'caveat' ))

            app.match[row][col] = wordGraphic

Random()


def onStep():
    prevX = rightB.centerX 
    rightB.centerX += rightBSpeed
    rightB2.centerX += rightBSpeed
    rightB3.centerX += rightBSpeed
    rightB4.centerX += rightBSpeed
    app.counter += 1
    if(app.counter == betweenCount):
        app.counter= 0
        if(rightB.visible == True):
            rightB.visible = False
            rightB2.visible = True
        elif(rightB2.visible == True):
            rightB2.visible = False
            rightB3.visible = True
        elif(rightB3.visible == True):
            rightB3.visible = False
            rightB4.visible = True
        elif(rightB4.visible == True):
            rightB4.visible = False
            rightB.visible = True
   
    if(Timer.stopped == False):
        Timer.value = rounded(time.time()-startTime)
    if(rightB.right - 5 >= leftB.left + 5):
        depth = (rightB.right - 5) - (leftB.left + 5)
        rightB.right -= depth/2
        leftB.left += depth/2

    if(rightB2.right - 5 >= leftB.left + 5):
        depth = (rightB2.right - 5) - (leftB.left + 5)
        rightB2.right -= depth/2
        leftB.left += depth/2

    if(rightB3.right - 5 >= leftB.left + 5):
        depth = (rightB3.right - 5) - (leftB.left + 5)
        rightB3.right -= depth/2
        leftB.left += depth/2
    
    if(rightB4.right - 5 >= leftB.left + 5):
        depth = (rightB4.right - 5) - (leftB.left + 5)
        rightB4.right -= depth/2
        leftB.left += depth/2

    if(prevX > rightB.centerX):
       rightB.visible = True
       rightB2.visible = False
       rightB3.visible = False
       rightB4.visible = False

        
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

                rightB.visible = True
                rightB2.visible = True
                rightB3.visible = True
                rightB4.visible = True

                pointer.toFront()
                rightB.toFront()
                rightB2.toFront()
                rightB3.toFront()
                rightB4.toFront()

                rightB.visible = True
                rightB2.visible = False
                rightB3.visible = False
                rightB4.visible = False

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
                    app.match[app.rowIndex][app.colIndex][app.charIndex].fill = 'gold'
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
