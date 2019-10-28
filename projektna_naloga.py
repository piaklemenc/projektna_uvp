import turtle
import math
import random

#zaslon
ozadje = turtle.Screen()
ozadje.bgcolor('black')
ozadje.bgpic('sea.gif')
ozadje.tracer(3) #figurce lepse tecejo, se ne zatikajo


#meje zaslona
okvir = turtle.Turtle()

okvir.penup()
okvir.speed(0)
okvir.setposition(-360, -380)
okvir.penup()
okvir.pensize(3)
for side in range(4):
    okvir.forward(740)
    okvir.left(90)
okvir.hideturtle()



#igralec1
zelvica = turtle.Turtle()
zelvica.shape('turtle')
zelvica.color('green')
zelvica.pencolor('black')
zelvica.penup() #da ne rise crte ko se zelvica premika
zelvica.speed(0) #da se ne ustavlja ko spreminjamo hitrost
zelvica.turtlesize(3)

#igralec2
zelvica2 = turtle.Turtle()
zelvica2.shape('turtle')
zelvica2.color('violet')
zelvica2.pencolor('black')
zelvica2.penup() 
zelvica2.speed(0) 
zelvica2.turtlesize(3)



#tocke
tocke = 0
tocke2 = 0


#hrana
maxhrana = 6
jedilnik = []

for count in range(maxhrana):
    jedilnik.append(turtle.Turtle())
    jedilnik[count].color('red')
    jedilnik[count].pencolor('lightblue')
    jedilnik[count].shape('circle')
    jedilnik[count].penup()
    jedilnik[count].speed(0)
    jedilnik[count].setposition(random.randint(-330, 330), random.randint(-330,330))

#strup
maxstrup = 4
strupi = []

for count in range(maxstrup):
    strupi.append(turtle.Turtle())
    strupi[count].color('darkblue')
    strupi[count].shape('circle')
    strupi[count].penup()
    strupi[count].speed(0)
    strupi[count].setposition(random.randint(-330, 330), random.randint(-330,330))
    

#hitrost, smer
hitrost = 1
hitrost2 = 1

#funkcije za smer in hitrost igralca1
def obrat_levo():
    zelvica.left(90)
def obrat_desno():
    zelvica.right(90)
def hitreje():
    global hitrost
    hitrost += 1
def pocasneje():
    global hitrost
    if hitrost > 1:
        hitrost -= 1
    
def dotik(s1, s2):
    d = math.sqrt(math.pow(s1.xcor() - s2.xcor(),2) + math.pow(s1.ycor() - s2.ycor(),2))
    if d < 30:
        return True
    else:
        return False

#funkcije za smer in hitrost igralca2
def obrat_levo2():
    zelvica2.left(90)
def obrat_desno2():
    zelvica2.right(90)
def hitreje2():
    global hitrost2
    hitrost2 += 1
def pocasneje2():
    global hitrost2
    if hitrost2 > 1:
        hitrost2 -= 1

#ukazi na tipkovnici za smer in hitrost igralca1
turtle.listen()
turtle.onkey(obrat_levo, 'Left')
turtle.onkey(obrat_desno, 'Right')
turtle.onkey(hitreje, 'Up')
turtle.onkey(pocasneje, 'Down')


#ukazi na tipkovnici za smer in hitrost igralca2
turtle.listen()
turtle.onkey(obrat_levo2, 's')
turtle.onkey(obrat_desno2, 'd')
turtle.onkey(hitreje2, 'e')
turtle.onkey(pocasneje2, 'x')



while True:
    zelvica.forward(hitrost)
    #meje zelvice1
    if zelvica.xcor() > 350 or zelvica.xcor() < -350:
        zelvica.right(180)
    if zelvica.ycor() > 350 or zelvica.ycor() < -350:
        zelvica.left(180)

    #meje zelvice2
    zelvica2.forward(hitrost2)
    if zelvica2.xcor() > 350 or zelvica2.xcor() < -350:
        zelvica2.right(180)
    if zelvica2.ycor() > 350 or zelvica2.ycor() < -350:
        zelvica2.left(180)
        



    #premikajoca hrana
    for count in range(maxhrana):
        jedilnik[count].forward(1)
        #meje hrane
        if jedilnik[count].xcor() > 350 or jedilnik[count].xcor() < -350:
            jedilnik[count].right(180)
        if jedilnik[count].ycor() > 350 or jedilnik[count].ycor() < -350:
            jedilnik[count].left(180)            
        #zelvica1 poje hrano
        if dotik(zelvica,jedilnik[count]):
            jedilnik[count].setposition(random.randint(-330, 330), random.randint(-330,330))
            jedilnik[count].right(random.randint(0,360))
            tocke += 1
            #tocke na ozadju igralca1
            okvir.undo() #da se stevilke tock ne pisejo ena na drugo
            okvir.penup()
            okvir.hideturtle()
            okvir.setposition(-340, 360)
            niz_tock = "Score1: %s" %tocke
            okvir.write(niz_tock,False, align="left", font=('Arial', 14, 'normal')) 
        #zelvica2 poje hrano
        if dotik(zelvica2,jedilnik[count]):
            jedilnik[count].setposition(random.randint(-330, 330), random.randint(-330,330))
            jedilnik[count].right(random.randint(0,360))
            tocke2 += 1
            #tocke na ozadju igralca2
            okvir.undo() #da se stevilke tock ne pisejo ena na drugo
            okvir.penup()
            okvir.hideturtle()
            okvir.setposition(-140, 360)
            niz_tock2 = "Score2: %s" %tocke2
            okvir.write(niz_tock2, False, align="left", font=('Arial', 14, 'normal'))

#-------------------------------
    #premikajoc strup
    for count in range(maxstrup):
        strupi[count].forward(1)
        #meje strupa
        if strupi[count].xcor() > 350 or jedilnik[count].xcor() < -350:
            strupi[count].right(180)
        if strupi[count].ycor() > 350 or jedilnik[count].ycor() < -350:
            strupi[count].left(180)
        #zelvica1 poje strup
        if dotik(zelvica,strupi[count]):
            strupi[count].setposition(random.randint(-330, 330), random.randint(-330,330))
            strupi[count].right(random.randint(0,360))
            tocke -= 1
            #tocke na ozadju igralca1
            okvir.undo() #da se stevilke tock ne pisejo ena na drugo
            okvir.penup()
            okvir.hideturtle()
            okvir.setposition(-340, 360)
            niz_tock = "Score1: %s" %tocke
            okvir.write(niz_tock,False, align="left", font=('Arial', 14, 'normal')) 
        #zelvica2 poje strup
        if dotik(zelvica2,strupi[count]):
            strupi[count].setposition(random.randint(-330, 330), random.randint(-330,330))
            strupi[count].right(random.randint(0,360))
            tocke2 -= 1
            #tocke na ozadju igralca2
            okvir.undo() #da se stevilke tock ne pisejo ena na drugo
            okvir.penup()
            okvir.hideturtle()
            okvir.setposition(-140, 360)
            niz_tock2 = "Score2: %s" %tocke2
            okvir.write(niz_tock2, False, align="left", font=('Arial', 14, 'normal'))
            
   


            
            
            









delay = raw_input('Press Enter to finish.')
