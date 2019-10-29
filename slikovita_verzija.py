import turtle
import math
import random

#zaslon
ozadje = turtle.Screen()
ozadje.bgcolor('black')
ozadje.bgpic('sea.gif')
ozadje.tracer(3)
ozadje.setup(900,900)


#meje zaslona
okvir = turtle.Turtle()
okvir.penup()
okvir.speed(0)
okvir.setposition(-360, -360)
okvir.penup()
okvir.pensize(3)
for side in range(4):
    okvir.forward(720)
    okvir.left(90)
okvir.hideturtle()

#shape
turtle.register_shape('shark.gif')
turtle.register_shape('riba1.gif')
turtle.register_shape('riba2.gif')

#igralec1
zelvica = turtle.Turtle()
zelvica.shape('turtle')
zelvica.color('green')
zelvica.pencolor('black')
zelvica.penup() 
zelvica.speed(0) 
zelvica.turtlesize(3)

#igralec2
zelvica2 = turtle.Turtle()
zelvica2.shape('turtle')
zelvica2.color('violet')
zelvica2.pencolor('black')
zelvica2.penup() 
zelvica2.speed(0) 
zelvica2.turtlesize(3)



#sovraznik
shark = turtle.Turtle()
shark.shape('shark.gif')
shark.speed(0)
shark.penup()
shark.turtlesize(3)
shark.setposition(150,100)



#tocke
tocke = 0
tocke2 = 0


#hrana
maxhrana = 6
jedilnik = []

for i in range(maxhrana):
    jedilnik.append(turtle.Turtle())
    jedilnik[i].shape('riba1.gif')
    jedilnik[i].penup()
    jedilnik[i].speed(0)
    jedilnik[i].setheading(60)
    jedilnik[i].setposition(random.randint(-330, 330), random.randint(-330,330))

#strup
maxstrup = 4
strupi = []

for j in range(maxstrup):
    strupi.append(turtle.Turtle())
    strupi[j].shape('riba2.gif')
    strupi[j].penup()
    strupi[j].speed(0)
    strupi[j].setheading(70)
    strupi[j].setposition(random.randint(-330, 330), random.randint(-330,330))
    

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
    if d < 40:
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
    if zelvica.xcor() > 340 or zelvica.xcor() < -340:
        zelvica.right(180)
    if zelvica.ycor() > 340 or zelvica.ycor() < -340:
        zelvica.left(180)

    #meje zelvice2
    zelvica2.forward(hitrost2)
    if zelvica2.xcor() > 340 or zelvica2.xcor() < -340:
        zelvica2.right(180)
    if zelvica2.ycor() > 340 or zelvica2.ycor() < -340:
        zelvica2.left(180)
        
    #meje sovraznika
    x = 2
    shark.forward(x)
    if shark.xcor() > 420 or shark.xcor() < -220:
        shark.right(180)
    if shark.ycor() > 340 or shark.ycor() < -340:
        shark.left(180)


    #premikajoca hrana
    for k in range(maxhrana):
        jedilnik[k].forward(1)
        #meje hrane
        if jedilnik[k].xcor() > 340 or jedilnik[k].xcor() < -340:
            jedilnik[k].right(180)
        if jedilnik[k].ycor() > 340 or jedilnik[k].ycor() < -340:
            jedilnik[k].left(180)            
        #zelvica1 poje hrano
        if dotik(zelvica,jedilnik[k]):
            jedilnik[k].setposition(random.randint(-330, 330), random.randint(-330,330))
            jedilnik[k].right(random.randint(0,360))
            tocke += 1
            #tocke na ozadju igralca1
            okvir.undo() 
            okvir.penup()
            okvir.hideturtle()
            okvir.setposition(-340, 360)
            niz_tock = "Score1: %s" %tocke
            okvir.write(niz_tock,False, align="left", font=('Arial', 14, 'normal')) 
        #zelvica2 poje hrano
        if dotik(zelvica2,jedilnik[k]):
            jedilnik[k].setposition(random.randint(-330, 330), random.randint(-330,330))
            #jedilnik[k].right(random.randint(0,360))
            tocke2 += 1
            #tocke na ozadju igralca2
            okvir.undo() 
            okvir.penup()
            okvir.hideturtle()
            okvir.setposition(-140, 360)
            niz_tock2 = "Score2: %s" %tocke2
            okvir.write(niz_tock2, False, align="left", font=('Arial', 14, 'normal'))

    #premikajoc strup
    for m in range(maxstrup):
        strupi[m].forward(1)
        #meje strupa
        if strupi[m].xcor() > 340 or strupi[m].xcor() < -340:
            strupi[m].right(180)
        if strupi[m].ycor() > 250 or strupi[m].ycor() < -400:
            strupi[m].left(180) 
        #zelvica1 poje strup
        if dotik(zelvica,strupi[m]):
            strupi[m].setposition(random.randint(-330, 330), random.randint(-330,330))
            strupi[m].right(random.randint(0,360))
            tocke -= 1
            #tocke na ozadju igralca1
            okvir.undo() 
            okvir.penup()
            okvir.hideturtle()
            okvir.setposition(-340, 360)
            niz_tock = "Score1: %s" %tocke
            okvir.write(niz_tock,False, align="left", font=('Arial', 14, 'normal'))
        if dotik(zelvica, shark) and tocke > 0:
            tocke = 0
            okvir.undo() 
            okvir.penup()
            okvir.hideturtle()
            okvir.setposition(-340, 360)
            niz_tock = "Score2: %s" %tocke
            okvir.write(niz_tock, False, align="left", font=('Arial', 14, 'normal'))

        
        #zelvica2 poje strup
        if dotik(zelvica2,strupi[m]):
            strupi[m].setposition(random.randint(-330, 330), random.randint(-330,330))
            strupi[m].right(random.randint(0,360))
            tocke2 -= 1
            #tocke na ozadju igralca2
            okvir.undo() 
            okvir.penup()
            okvir.hideturtle()
            okvir.setposition(-140, 360)
            niz_tock2 = "Score2: %s" %tocke2
            okvir.write(niz_tock2, False, align="left", font=('Arial', 14, 'normal'))

        if dotik(zelvica2, shark) and tocke2 > 0:
            tocke2 = 0
            okvir.undo()
            okvir.penup()
            okvir.hideturtle()
            okvir.setposition(-140, 360)
            niz_tock2 = "Score2: %s" %tocke2
            okvir.write(niz_tock2, False, align="left", font=('Arial', 14, 'normal'))

            










