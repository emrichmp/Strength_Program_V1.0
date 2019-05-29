# Strength Program
# StrengthProgram.py
# Emrich-Michael Perrier
# Emrich
# eperrier

from graphics import *
from random import randrange

def Win():
#Sets up graphics window to draw and display program
    #GW
    win = GraphWin("Final",1500,900)
    win.setBackground("tan")
    win.setCoords(0,0,15,9)
    return win
 
def Page(win):
#Sets up page with button, labels and make graphic organizer structure of the program
    #OTXT
    schedule = Rectangle(Point(5,0.5), Point(14.5,8.5))
    schedule.setFill("white")
    schedule.draw(win)
    weight = Text(Point(1,7.7), "Weight:")
    weight.draw(win)
    squat = Text(Point(1,7.2), "Squat:")
    squat.draw(win)
    bench = Text(Point(1,6.7), "Bench:")
    bench.draw(win)
    deadlift = Text(Point(1,6.2), "Deadlift:")
    deadlift.draw(win)
    title = Text(Point(2.5,8.3),"Powerlifting Strength Program")
    title.setSize(20)
    title.draw(win)
    prompt = Text(Point(1.5,4.8),"*Put in information and click GO!*")
    prompt.draw(win)
    prompt2 = Text(Point(2.3,4.6),"All lifts should be followed by accessory work of your choice")
    prompt2.draw(win)
    prompt3 = Text(Point(2.4,4.4),"Program is made with assumption that user is an intermediate lifter")
    prompt3.draw(win)
    go = Rectangle(Point(0.7,5.8),Point(4,5.2))
    go.setFill("green")
    go.draw(win)
    go_text = Text(Point(2.4,5.5),"GO")
    go_text.draw(win)
    
def lift(win):
#Function labels the name of the lift for that day on that week using for loops
#for loop to write bench press on page
    #OTXT
        wy = 7.95
        for i in range(4):
            wt = ("Bench Press")
            week = Text(Point(5.4,wy), wt)
            week.setSize(10)
            week.draw(win)
            wy= wy-2
        #for loop to write deadlift on page
        wy = 7.95
        for i in range(4):
            wt = ("Deadlift")
            week = Text(Point(6.9,wy), wt)
            week.setSize(10)
            week.draw(win)
            wy= wy-2
        #for loop to write squat on page
        wy = 7.95
        for i in range(4):
            wt = ("Squat")
            week = Text(Point(8.4,wy), wt)
            week.setSize(10)
            week.draw(win)
            wy= wy-2
        #for loop to write pause bench on page
        wy = 7.95
        for i in range(4):
            wt = ("Pause Bench")
            week = Text(Point(9.9,wy), wt)
            week.setSize(10)
            week.draw(win)
            wy= wy-2
        #for loop to write sumo deadlift on page
        wy = 7.95
        for i in range(4):
            wt = ("Sumo Deadlift")
            week = Text(Point(11.4,wy), wt)
            week.setSize(10)
            week.draw(win)
            wy= wy-2
        #for loop to explain to use accessory movements after your workout
        wy = 7
        for i in range(4):
            wt = ("Follow main lift with accessory work of your choice in a 4x10 set and rep scheme")
            week = Text(Point(8.7,wy), wt)
            week.setSize(15)
            week.draw(win)
            wy= wy-2

def setsxreps(win):
#Class to make structure of the page for the programing for the sets and reps of the lifts and the week
#classes use for loops to write set and rep schemes that the program follows from week to week
    #OTXT
        wy = 8.3
        cy = 8.15
        for i in range(4):
            wt = ("Week", i+1)
            week = Text(Point(5.4,wy), wt)
            week.draw(win)
            wy= wy-2
        for i in range(4):
            r = Text(Point(13.5,cy), "Random")
            r.setSize(10)
            r.draw(win)
            cy = cy -2
        wx = 5.4
        for i in range(5):
            w1 = Text(Point(wx,7.8),"4x10 @ ")
            w1.setSize(10)
            w1.draw(win)
            wx = wx + 1.5
        wx = 5.4
        for i in range(5):
            w2 = Text(Point(wx,5.8),"5x8 @ ")
            w2.setSize(10)
            w2.draw(win)
            wx = wx + 1.5
        wx = 5.4
        for i in range(5):
            w2 = Text(Point(wx,3.8),"6x3 @ ")
            w2.setSize(10)
            w2.draw(win)
            wx = wx + 1.5
        wx = 5.4
        for i in range(5):
            w2 = Text(Point(wx,1.8),"7x2 @ ")
            w2.setSize(10)
            w2.draw(win)
            wx = wx + 1.5

def label(case,day,move,win):
#case and day is if its a push or pull day 1 or 2, move is how much on the graph win the label is moving
#Class to make structure of the page for the programing. ie if it is a push, pull or leg day
#Labels if the day of that week is a push or pull day 1 or 2 and prints the leg day every week
    #OTXT
        cy = 8.15
        if case == "push":
            for i in range(4):
                ct = ("Push", day)
                c = Text(Point(5.4+move,cy), ct)
                c.setSize(10)
                c.draw(win)
                cy = cy-2
        elif case == "pull":
            for i in range(4):
                ct = ("Pull", day)
                c = Text(Point(6.9+move,cy), ct)
                c.setSize(10)
                c.draw(win)
                cy = cy-2
        elif case == "leg":
            for i in range(4):
                ct = ("Leg", day)
                c = Text(Point(8.4,cy), ct)
                c.setSize(10)
                c.draw(win)
                cy = cy-2
                
def Structure(win):
#calls label functions to make the structure of the graph
    #FNC
    lift(win)
    label("push",1,0,win)
    label("pull",1,0,win)
    label("leg",1,0,win)
    label("push",2,4.55,win)
    label("pull",2,4.5,win)
    
def push(b):
    #b value is your bench press one rep max
    #Calculates the weight that should be used for a bench press or bench variations for push days
    #program follows a higher weight for more sets for less reps each week at an increase of 10% of 1 rep max weight
    #p1w1
    p1w1 = b//1.5
    #p1w2
    p1w2 = b//1.4
    #p1w3
    p1w3 = b//1.3
    #p1w4
    p1w4 = b//1.2
    #p2w1
    p2w1 = p1w1-10
    #p2w2
    p2w2 = p1w2-10
    #p2w3
    p2w3 = p1w3-10
    #p2w4
    p2w4 = p1w4-10
    return p1w1,p1w2,p1w3,p1w4,p2w1,p2w2,p2w3,p2w4

def sq(s):
    #s value is your your squat one rep max
    #Calculates the weight that should be used for squats for leg days
    #program follows a higher weight for more sets for less reps each week at an increase of 10% of 1 rep max weight
    #lw1
    lw1 = s//1.5
    #lw2
    lw2 = s//1.4
    #lw3
    lw3 = s//1.3
    #lw4
    lw4 = s//1.2
    return lw1,lw2,lw3,lw4
    
def pull(d):
    #d value is your deadlift one rep max
    #Calculates the weight that should be used for deadlifts for pull days
    #program follows a higher weight for more sets for less reps each week at an increase of 10% of 1 rep max weight
    #p1w1
    pl1w1 = d//1.5
    #p1w2
    pl1w2 = d//1.4
    #p1w3
    pl1w3 = d//1.3
    #p1w4
    pl1w4 = d//1.2
    #p2w1
    pl2w1 = pl1w1-20
    #p2w2
    pl2w2 = pl1w2-20
    #p2w3
    pl2w3 = pl1w3-20
    #p2w4
    pl2w4 = pl1w4-20
    return pl1w1,pl1w2,pl1w3,pl1w4,pl2w1,pl2w2,pl2w3,pl2w4
    
def random():
#basic randrange function
    #RND
    d = randrange(0,6)
    return d

def gymday(win):
#makes aList of gym days and calls random 4 times to show your once a week random gym day
    #LOOD
    dList = ["Arm day","Ab day", "Cardio day", "Shoulder day", "Chest Day", "Back Day", "Leg Day"]
    #RND
    r1 = random()
    gymDay1 = Text(Point(13.5,7.8),dList[r1])
    gymDay1.draw(win)
    r2 = random()
    gymDay2 = Text(Point(13.5,5.8),dList[r2])
    gymDay2.draw(win)
    r3 = random()
    gymDay3 = Text(Point(13.5,3.8),dList[r3])
    gymDay3.draw(win)
    r4 = random()
    gymDay4 = Text(Point(13.5,1.8),dList[r4])
    gymDay4.draw(win)
    
def pushweight(p1w1,p1w2,p1w3,p1w4,p2w1,p2w2,p2w3,p2w4,win):
#The pw values are the amount of weight that needs to be lifted for that push day
#Function displays the weight needed for certain push days in the window
    #OTXT
    push1w1 = Text(Point(5.4,7.6),(p1w1,"lbs"))
    push1w1.draw(win)
    push1w2 = Text(Point(5.4,5.6),(p1w2,"lbs"))
    push1w2.draw(win)
    push1w3 = Text(Point(5.4,3.6),(p1w3,"lbs"))
    push1w3.draw(win)
    push1w4 = Text(Point(5.4,1.6),(p1w4,"lbs"))
    push1w4.draw(win)
    push2w1 = Text(Point(10,7.6),(p2w1,"lbs"))
    push2w1.draw(win)
    push2w2 = Text(Point(10,5.6),(p2w2,"lbs"))
    push2w2.draw(win)
    push2w3 = Text(Point(10,3.6),(p2w3,"lbs"))
    push2w3.draw(win)
    push2w4 = Text(Point(10,1.6),(p2w4,"lbs"))
    push2w4.draw(win)

def pullweight(pl1w1,pl1w2,pl1w3,pl1w4,pl2w1,pl2w2,pl2w3,pl2w4,win):
#The plw values are the amount of weight that needs to be lifted for that pull day
#Function displays the weight needed for certain pull days in the window
    #OTXT
    pull1w1 = Text(Point(6.8, 7.6),(pl1w1,"lbs"))
    pull1w1.draw(win)
    pull1w2 = Text(Point(6.8, 5.6),(pl1w2,"lbs"))
    pull1w2.draw(win)
    pull1w3 = Text(Point(6.8, 3.6),(pl1w3,"lbs"))
    pull1w3.draw(win)
    pull1w4 = Text(Point(6.8, 1.6),(pl1w4,"lbs"))
    pull1w4.draw(win)
    pull2w1 = Text(Point(11.4, 7.6),(pl2w1,"lbs"))
    pull2w1.draw(win)
    pull2w2 = Text(Point(11.4, 5.6),(pl2w2,"lbs"))
    pull2w2.draw(win)
    pull2w3 = Text(Point(11.4, 3.6),(pl2w3,"lbs"))
    pull2w3.draw(win)
    pull2w4 = Text(Point(11.4, 1.6),(pl2w4,"lbs"))
    pull2w4.draw(win)

def legweight(lw1,lw2,lw3,lw4,win):
#The lw values are the amount of weight that needs to be lifted for that leg day
#Function displays the weight needed for certain leg days in the window
    #OTXT
    leg1 = Text(Point(8.4, 7.6),(lw1,"lbs"))
    leg1.draw(win)
    leg2 = Text(Point(8.4, 5.6),(lw2,"lbs"))
    leg2.draw(win)
    leg3 = Text(Point(8.4, 3.6),(lw3,"lbs"))
    leg3.draw(win)
    leg4 = Text(Point(8.4, 1.6),(lw4,"lbs"))
    leg4.draw(win)

def button(win):
#Calls the entry points and the button collison and executes the math functions and display functions when button is pressed
    #IEB
    weight = Entry(Point(1.5,7.7),3)
    weight.draw(win)
    bench = Entry(Point(1.5,6.7),3)
    bench.draw(win)
    squat = Entry(Point(1.5, 7.17),3)
    squat.draw(win)
    deadlift = Entry(Point(1.5, 6.2),3)
    deadlift.draw(win)
    #IMS
    clickPoint = win.getMouse()
    xClick = clickPoint.getX()
    yClick = clickPoint.getY()
    if xClick>0.7 and xClick<4 and yClick>5.2 and yClick<5.8:
        setsxreps(win)
        gymday(win)
        w = float(weight.getText())
        b = float(bench.getText())
        s = float(squat.getText())
        d = float(deadlift.getText())
        p1w1,p1w2,p1w3,p1w4,p2w1,p2w2,p2w3,p2w4 = push(b)
        lw1,lw2,lw3,lw4 = sq(s)
        pl1w1,pl1w2,pl1w3,pl1w4,pl2w1,pl2w2,pl2w3,pl2w4 = pull(d)
        pushweight(p1w1,p1w2,p1w3,p1w4,p2w1,p2w2,p2w3,p2w4,win)
        pullweight(pl1w1,pl1w2,pl1w3,pl1w4,pl2w1,pl2w2,pl2w3,pl2w4,win)
        legweight(lw1,lw2,lw3,lw4,win)
        outText = Text(Point(2.5,4.2),"Check output file called 'powerlift_comparison.txt' to see your lifts compared to a pro!")
        outText.setSize(10)
        outText.draw(win)
        total = b + s + d
        #FNC
        files(w,total)

def files(weight, total):
#weight is the weight of the user and total is the combine total of all lifts of the user
#Function takes your weight from the button function, compares your weight and your lift total to the worlds strongest powerlifter and prints it to and output file
    #IFL
    infile = open("LiftRecord.txt", "r")
    records = infile.readline()
    records = records.split()
    tcompare = int(records[3])-total
    wcompare = int(records[2])-weight
    #OFL
    outfile = open("powerlift_comparison.txt","w")
#comparison of your total to the strongest lifter in the worlds total is put into an output file for your viewing
    print("your lift total is", tcompare,"pounds less than the total of", records [0], records[1], "and you're", wcompare, "pounds lighter than him", file = outfile)

class weight:
#Class decide make either a picture of a dumbell or barbell that is printed into the shell
    #CLOD
    def __init__(self, weight):
        self.weight = weight
    def gymWeight(self):
        if self.weight == 1:
            print("This is a dumbbell:")
            print("*   *")
            print("*****")
            print("*   *")
        if self.weight == 2:
            print("This is a barbell:")
            print("*                 *")
            print("*                 *")
            print("*******************")
            print("*                 *")
            print("*                 *")
            
def main():
#Calls all the functions
    w = Win()
    Page(w)
    Structure(w)
    dumbbell = weight(1)
    dumbbell.gymWeight()
    barbell = weight(2)
    barbell.gymWeight()
    button(w)
main()