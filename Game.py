from colorsys import ONE_THIRD
from turtle import Turtle
from typing import KeysView
from cmu_graphics import * 
import time

app.title = "Tjo katt"
app.stepsPerSecond = 60
app.background = 'darkSlateGrey'
app.start= False

Timer = Label('0', 30,25, fill = 'white', size = 40)
startTime = time.time()
Timer.stopped = False
app.totalChars = 0
wpm = Label('0', 360,25, fill = 'white', size = 40)
wpmText = Label('WPM:', 300, 25, fill = 'white', size = 20 )
ground = Group(

    
    Rect(-10,220,420,200, fill = 'black', border = 'white', borderWidth = 5)

)

import os
thisFolder = os.path.dirname(os.path.realpath(__file__))

leftB = Image(thisFolder + '/bullleft1.png', 255,139, height = 90, width = 120)

leftB2 = Image(thisFolder + '/bullleft3.png', 255,139, height = 90, width = 120)

leftB3 = Image(thisFolder + '/bullleft2.png', 255,139, height = 90, width = 120)

leftB4 = Image(thisFolder + '/bullleft2.png', 255,139, height = 90, width = 120)


rightB = Image(thisFolder + '/bullright1.png',55,139, height = 90, width = 120)

rightB2 = Image(thisFolder + '/bullright3.png', 55,139, height = 90, width = 120)

rightB3 = Image(thisFolder + '/bullright2.png', 55,139, height = 90, width = 120)

rightB4 = Image(thisFolder + '/bullright2.png', 55,139, height = 90, width = 120)

rightbullwin = Image(thisFolder + '/rightbullwin.png', 23,0, height = 400, width = 350)
rightw = Rect(0,0,400,400, fill = 'white')
rightlabel = Label('Ur Dead',200,350, fill = 'red', size = 40, font = 'robotomono')

rightB.visible = True
rightB2.visible = False
rightB3.visible = False
rightB4.visible = False
rightbullwin.visible = False
rightlabel.visible = False
rightw.visible = False
leftB.visible = True
leftB2.visible = False
leftB3.visible = False
leftB4.visible = False


rightBSpeed = 0.35
leftBSpeed = 0
pointer = Group(

    Line(52,254,52, 274, fill = 'White' ) 

)

rightB.rotateAngle = 5
rightB2.rotateAngle = 5
rightB3.rotateAngle = 5
rightB4.rotateAngle = 5
leftB.rotateAngle = -5
leftB2.rotateAngle = -5
leftB3.rotateAngle = -5
leftB4.rotateAngle = -5

lables = Group
app.counter = 0
app.wpmcounter = 0
betweenwpm = 3
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
def animation():
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

        if(leftB.visible == True):
            leftB.visible = False
            leftB2.visible = True
        elif(leftB2.visible == True):
            leftB2.visible = False
            leftB3.visible = True
        elif(leftB3.visible == True):
            leftB3.visible = False
            leftB4.visible = True
        elif(leftB4.visible == True):
            leftB4.visible = False
            leftB.visible = True

    

def speed():
    app.speedcount += 1
    if(app.speedcount > 50):
        leftBSpeed = 0
    else:
        leftBSpeed = int(wpm.value) / 25

    leftprevX = leftB.centerX
    
    leftB.centerX -= leftBSpeed
    leftB2.centerX -= leftBSpeed
    leftB3.centerX -= leftBSpeed
    leftB4.centerX -= leftBSpeed
    
    prevX = rightB.centerX 
    rightB.centerX += rightBSpeed
    rightB2.centerX += rightBSpeed
    rightB3.centerX += rightBSpeed
    rightB4.centerX += rightBSpeed
    app.counter += 1
    app.wpmcounter += 1
    
def collison():
    if(Timer.stopped == False):
        Timer.value = rounded(time.time()-startTime)
    if(rightB.right - 5 >= leftB.left + 5):
        depth = (rightB.right - 5) - (leftB.left + 5)
        rightB.right -= depth/2
        leftB.left += depth/2
        leftB2.left += depth/2
        leftB3.left += depth/2
        leftB4.left += depth/2

    if(rightB2.right - 5 >= leftB.left + 5):
        depth = (rightB2.right - 5) - (leftB.left + 5)
        rightB2.right -= depth/2
        leftB.left += depth/2
        leftB2.left += depth/2
        leftB3.left += depth/2
        leftB4.left += depth/2

    if(rightB3.right - 5 >= leftB.left + 5):
        depth = (rightB3.right - 5) - (leftB.left + 5)
        rightB3.right -= depth/2
        leftB.left += depth/2
        leftB2.left += depth/2
        leftB3.left += depth/2
        leftB4.left += depth/2

    if(rightB4.right - 5 >= leftB.left + 5):
        depth = (rightB4.right - 5) - (leftB.left + 5)
        rightB4.right -= depth/2
        leftB.left += depth/2
        leftB2.left += depth/2
        leftB3.left += depth/2
        leftB4.left += depth/2

    if(prevX > rightB.centerX):
       rightB.visible = True
       rightB2.visible = False
       rightB3.visible = False
       rightB4.visible = False

    leftprevX = leftB.centerX

    if(leftprevX < leftB.centerX):
        leftB.visible = True
        leftB2.visible = False
        leftB3.visible = False
        leftB4.visible = False

def winlose():
    if(rightB.right <= 0 ):
        Timer.stopped = True
        
    if(leftB.left >= 400):
        Timer.stopped = True

        rightbullwin.visible = True
        rightw.visible = True
        rightlabel.visible = True
        rightw.toFront()
        rightbullwin.toFront()
        rightlabel.toFront()

def onstepwpm():
    if(app.wpmcounter == betweenwpm):
        app.wpmcounter = 0
        wpm.value = rounded(((app.totalChars/5)/(time.time() - startTime))*60)

app.rows = 4
app.cols = 5

app.gameWords = makeList(app.rows, app.cols)

app.rowIndex = 0
app.colIndex = 0
app.charIndex = 0
prevX = 0
app.match = makeList(app.rows,app.cols)

app.speedcount = 0

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
    if app.start == True:
        speed()
        animation()
        collison()
        winlose()
        onstepwpm()

def onKeyPress(key):
    if key == 'enter':
        app.start = True
    if(app.start == True):
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
                        app.totalChars += 1
                        app.match[app.rowIndex][app.colIndex][app.charIndex].fill = 'gold'
                        app.speedcount = 0
                    else:
                        app.match[app.rowIndex][app.colIndex][app.charIndex].fill = 'red'
                    pointer.centerX = app.match[app.rowIndex][app.colIndex][app.charIndex].centerX + app.match[app.rowIndex][app.colIndex][app.charIndex].width/2
                    pointer.centerY = app.match[app.rowIndex][app.colIndex][app.charIndex].centerY
    
                    app.charIndex += 1                 

            else:
                app.rowIndex += 1
                app.colIndex = 0
    

    

cmu_graphics.run()
