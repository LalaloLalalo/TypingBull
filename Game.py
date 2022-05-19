from cmu_graphics import * 


app.background = rgb(0, 206, 209)


ground = Group(
    
    Rect(0,220,400,180, fill = 'darkSlateGrey')

)

lables = Group
app.words = [['from', 'going','penis'],
['about','their', 'will', 'would'],
['make', 'just', 'think', 'time'],
['take', 'year', 'them'],
['want', 'when', 'which'],
['like', 'other', 'could'],
['into','here', 'then', 'than', 'look'],
['more', 'these', 'thing', 'well'], 
['also','good'],
['first', 'find', 'give'],
['need', 'back', 'even']]

app.char = []

app.rowIndex = 0
app.colIndex = 0
app.charIndex = 0

app.rows = 4
app.cols = 5
app.match = makeList(app.rows,app.cols)

def Random():
    for row in range(app.rows):
        for col in range(app.cols):
            centerX = 56 + col * 60
            centerY = 270 + row * 30
            randomcol = choice(app.words)
            randomword = choice(randomcol)
            app.match.append(Label(randomword,centerX,centerY, fill = 'white', font = 'orbitron', size = 19,align = 'left'))

Random()

def onKeyPress(key):
    if(app.rowIndex < app.rows):
        if(app.colIndex < app.cols):
            if(app.charIndex >= len(app.words[app.rowIndex][app.colIndex])):
                app.charIndex = 0
                app.colIndex += 1
            if(app.words[app.rowIndex][app.colIndex][app.charIndex] == key):
                #app.words[app.rowIndex][app.colIndex].fill = 'green'
                pass

            else:
               # app.words[app.rowIndex][app.colIndex].fill = 'red'
                pass
            app.charIndex += 1

        else:
            app.rowIndex += 1
            app.colIndex = 0

    
        
    '''if 'tab' in key:
        Random()'''



cmu_graphics.run()
