magicians = ['allice', 'david', 'carolina']
greatMagicians = []

def showMagicians(magiNames):
    for name in magiNames:
        print(name)

def makeGreat(notGreatYet, nowGreat):
    for name in notGreatYet:
        nowGreat.append(name.title() + ' the Great')

makeGreat(magicians, greatMagicians)
showMagicians(greatMagicians)

