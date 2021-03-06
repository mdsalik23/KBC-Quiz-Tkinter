from tkinter import *            #To use python GUI tkinter module is to be used
from PIL import ImageTk,Image    #To put images on the screen
import tkinter.font as f         #To style and resize font of the text in program
from datetime import date        #To calculate the current date and time of when the game was played
import sqlite3         #To connect program with database containing questions and answers
import random                  #To put out questions and their respective answers in a random sequence
import winsound                #To play audio in the program
import sys                     #Only to use exit command in the program

#DEFINING A CONNECTION B/W PYTHON AND MYSQL
con = sqlite3.connect("kbc.db")
mycursor = con.cursor()        #main cursor to execute mysql querries
con.commit()

#VARIABLE ASSIGNMENT FOR CURRENT DATE AND TIME
today = date.today()
    

#INITIALISING THE TKINTER GUI WINDOW-----------------------------
root = Tk()
root.title("KBC")
root.configure(background="#8B008B")
root.geometry("1920x1080")
root.attributes('-fullscreen', True)

#DEFINING VARIBALE FOR CHANGING FONT
myfont = f.Font(family='Maiandra GD')
myfontH = f.Font(family='Maiandra GD', size=30)


#KBC LCK F



#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#    SSSSSSSSSSS    TTTTTTTTTTTT      AA       RRRRRRRRRRRRR   TTTTTTTTTTTT    
#    SSSSSSSSSSS    TTTTTTTTTTTT     AAAA      RRR       RRR   TTTTTTTTTTTT    
#    SSSS                TTT        AA  AA     RRR       RRR        TTT        
#    SSSS                TTT       AA    AA    RRRRRRRRRRRRR        TTT        
#    SSSSSSSSSSS         TTT       AAAAAAAA    RRRRR                TTT    
#    SSSSSSSSSSS         TTT       AA    AA    RRR RRR              TTT     
#           SSSS         TTT       AA    AA    RRR   RRR            TTT    
#           SSSS         TTT       AA    AA    RRR     RRR          TTT      
#    SSSSSSSSSSS         TTT       AA    AA    RRR       RRR        TTT        
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
def start():
    winsound.PlaySound('btn.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)     #BUTTON CLICK SOUND
    
    global name                     #ASSIGNING GLOABAL VARIABLES THAT CAN BE USED ANYWHERE THROUGH OUT THE PROGRAM
    global age                      #THESE VARIABLES STORE THE CURRENT PLAYERS PERSONAL INFORMATION
    global ageINT
    global state
    name = nameE.get()              #PLAYER'S NAME
    try:
        ageINT = int(ageE.get())    #PLAYER'S AGE
        age = str(ageINT)           
    except ValueError:              #IF AGE IS IN STRING FORMAT THEN DEFAULT AGE IS 17
        ageINT = 17
        age = "17"
    state = stateE.get()              #PLAYER'S state

    head.place_forget()             #REMOVING ALL
    button.place_forget()           #WIDGETS FROM
    mainfrm.place_forget()          #HOME PAGE
    namel.place_forget()
    nameE.place_forget()
    agel.place_forget()
    ageE.place_forget()
    statel.place_forget()
    stateE.place_forget()


    
    #DEFINING VARIBALE FOR CHANGING FONT
    global myfont
    global myfontH
    myfont = f.Font(family='Maiandra GD')
    myfontH = f.Font(family='Maiandra GD', size=30)


                                                              #----------------------------------------
    #---------------------------------------------------------#||DEFINING STRUCTURE OF QUESTION PANEL||----------------------------------------------------------------#
                                                              #----------------------------------------
    #INTRODUCTION TEXT
    global e1
    frame1 = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    frame1.place(relwidth=0.66,relheight=0.16, relx=0.06, rely=0.03)
    e1 = Text(frame1, bg="#5B0A91", font=myfont, fg="white")
    e1.place(relwidth=1, relheight=1)

    #QUESTION NUMBER
    global e2
    frame2i = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    frame2i.place(relwidth=0.12, relheight=0.2, relx=0.06, rely=0.23)
    e2 = Entry(frame2i, bg="#5B0A91", font=myfont, fg="white")
    e2.place(relwidth=1, relheight=1)

    #QUESTION
    global e3
    frame2ii = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    frame2ii.place(relwidth=0.52, relheight=0.2, relx=0.2, rely=0.23)
    e3 = Entry(frame2ii, bg="#5B0A91", font=myfont, fg="white")
    e3.place(relwidth=1, relheight=1)


    #OPTION - A
    global OA
    global BA
    global frameBA
    frameBA = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    frameBA.place(relwidth=0.03, relheight=0.07, relx=0.08, rely=0.46)
    BA = Button(frameBA, bg="#5B0A91", text="A", fg="white", font=myfont, command=OPTIONA)
    BA.place(relwidth=1, relheight=1)

    frameOA = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    frameOA.place(relwidth=0.15, relheight=0.07, relx=0.12, rely=0.46)
    OA = Entry(frameOA, bg="#C5B358", font=myfont)
    OA.place(relwidth=1, relheight=1)


    #OPTION - B
    global OB
    global BB
    global frameBB
    frameBB = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    frameBB.place(relwidth=0.03, relheight=0.07, relx=0.3, rely=0.46)
    BB = Button(frameBB, bg="#5B0A91", text="B", fg="white", font=myfont, command=OPTIONB)
    BB.place(relwidth=1, relheight=1)

    frameOB = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    frameOB.place(relwidth=0.15, relheight=0.07, relx=0.34, rely=0.46)
    OB = Entry(frameOB, bg="#C5B358", font=myfont)
    OB.place(relwidth=1, relheight=1)


    #OPTION - C
    global OC
    global BC
    global frameBC  
    frameBC = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    frameBC.place(relwidth=0.03, relheight=0.07, relx=0.08, rely=0.56)
    BC = Button(frameBC, bg="#5B0A91", text="C", fg="white", font=myfont, command=OPTIONC)
    BC.place(relwidth=1, relheight=1)

    frameOC = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    frameOC.place(relwidth=0.15, relheight=0.07, relx=0.12, rely=0.56)
    OC = Entry(frameOC, bg="#C5B358", font=myfont)
    OC.place(relwidth=1, relheight=1)


    #OPTION - D
    global OD
    global BD
    global frameBD
    frameBD = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    frameBD.place(relwidth=0.03, relheight=0.07, relx=0.3, rely=0.56)
    BD = Button(frameBD, bg="#5B0A91", text="D", fg="white", font=myfont, command=OPTIOND)
    BD.place(relwidth=1, relheight=1)

    frameOD = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    frameOD.place(relwidth=0.15, relheight=0.07, relx=0.34, rely=0.56)
    OD = Entry(frameOD, bg="#C5B358", font=myfont)
    OD.place(relwidth=1, relheight=1)


    #DISPLAY OPTION
    global displ
    global dispopt
    displ = Frame(root, bg="#5B0A91", bd=10, relief="solid")
    displ.place(relwidth=0.16, relheight=0.07, relx=0.53, rely=0.46)
    dispopt = Entry(displ, bg="#C5B358", font=myfont)
    dispopt.place(relwidth=1, relheight=1)


    #LOCK BUTTON
    global lockf
    global lockb
    lockf = Frame(root, bg="#C5B358", bd=10, relief="groove")
    lockf.place(relwidth=0.16, relheight=0.07, relx=0.53, rely=0.56)
    lockb = Button(lockf, bg="#5B0A91", fg="white", font=myfont, text="LOCK", state=DISABLED)
    lockb.place(relwidth=1, relheight=1)


    #CONFIRM BUTTON
    global conff
    global confb
    conff = Frame(root, bg="#C5B358", bd=10, relief="groove")
    conff.place(relwidth=0.18, relheight=0.07, relx=0.53, rely=0.66)
    confb = Button(conff, bg="#5B0A91", fg="white", font=myfont, text="CONFIRM", state=DISABLED)
    confb.place(relwidth=1, relheight=1)

    
    #YOUR ANSWER IS.....
    global your
    global eyour
    your = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    your.place(relwidth=0.45, relheight=0.07, relx=0.06, rely=0.66)
    eyour = Entry(your, bg="#5B0A91", fg="white", font=myfont, text="YOUR ANSWER IS ...")
    eyour.place(relwidth=1, relheight=1)


    #CORRECT OR INCORRECT
    global corr
    global ecorr
    corr = Frame(root, bg="grey", bd=10, relief="ridge")
    corr.place(relwidth=0.25, relheight=0.2, relx=0.06, rely=0.76)
    myfont = f.Font(family='Maiandra GD', size=46, weight="bold")
    ecorr = Entry(corr, bg="#5B0A91", fg="white", font=myfont)
    ecorr.place(relwidth=1, relheight=1)


    #ACTUAL ANSWER
    global act
    global tact
    act = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    act.place(relwidth=0.38, relheight=0.2, relx=0.33, rely=0.76)
    tact = Text(act, bg="#5B0A91", font=myfont, fg="white")
    tact.place(relwidth=1, relheight=1)



    #MONEY COUNTER
    global moneyf
    global rup
    global moneye
    myfont = f.Font(family='Maiandra GD')
    moneyf = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    moneyf.place(relx=0.74, rely=0.03, relwidth=0.19, relheight=0.08)
    rup = Label(moneyf, bg="#5B0A91", fg="white", font=myfont , relief="raised", text="₹")
    rup.place(relx=0.015, rely=0.04, relwidth=0.3, relheight=0.85)
    moneye = Entry(moneyf, bg="white", font=myfont,relief="sunken")
    moneye.place(relx=0.35, rely=0.04, relwidth=0.635, relheight=0.85)


    #QUESTION LIST
    global ecanv
    qlist = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    qlist.place(relx=0.74, rely=0.15, relwidth=0.19, relheight=0.58)
    ecanv = Canvas(qlist)
    ecanv.place(relwidth=1, relheight=1)
    x=0.060375
    h=0.002
    rh=0.0595
    myfont = f.Font(family='Maiandra GD', weight="bold")
    
      
    m16 = "7 CRORE" 
    m15 = "1 CRORE" 
    m14 = "50,00,000"
    m13 = "25,00,000"
    m12 = "12,50,000"
    m11 = "6,40,000"
    m10 = "3,20,000"
    m9 = "1,60,000"
    m8 = "80,000"  
    m7 = "40,000"  
    m6 = "20,000"  
    m5 = "10,000"  
    m4 = "5,000"   
    m3 = "3,000"   
    m2 = "2,000"
    m1 = "1,000" 
   
    global mon16
    global q16
    mon16 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m16, font=myfont, anchor=E)
    mon16.place(relwidth=0.8, relx=0.2, relheight=rh, rely=h)
    q16 = Label(ecanv, bg="#5B0A91", fg="white", text="Q16", font=myfont, anchor=W)
    q16.place(relwidth=0.2, relheight=rh, rely=h)
    
    global mon15
    global q15
    mon15 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m15, font=myfont, anchor=E)
    mon15.place(relwidth=0.8, relx=0.2, relheight=rh, rely=x+h+h)
    q15 = Label(ecanv, bg="#5B0A91", fg="white", text="Q15", font=myfont, anchor=W)
    q15.place(relwidth=0.2, relheight=rh, rely=x+h+h)
    
    global mon14
    global q14
    mon14 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m14, font=myfont, anchor=E)
    mon14.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(2*x)+(3*h))
    q14 = Label(ecanv, bg="#5B0A91", fg="white", text="Q14", font=myfont, anchor=W)
    q14.place(relwidth=0.2, relheight=rh, rely=(2*x)+(3*h))
    
    global mon13
    global q13
    mon13 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m13, font=myfont, anchor=E)
    mon13.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(3*x)+(4*h))
    q13 = Label(ecanv, bg="#5B0A91", fg="white", text="Q13", font=myfont, anchor=W)
    q13.place(relwidth=0.2, relheight=rh, rely=(3*x)+(4*h))
    
    global mon12
    global q12
    mon12 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m12, font=myfont, anchor=E)
    mon12.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(4*x)+(5*h))
    q12 = Label(ecanv, bg="#5B0A91", fg="white", text="Q12", font=myfont, anchor=W)
    q12.place(relwidth=0.2, relheight=rh, rely=(4*x)+(5*h))
    
    global mon11
    global q11
    mon11 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m11, font=myfont, anchor=E)
    mon11.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(5*x)+(6*h))
    q11 = Label(ecanv, bg="#5B0A91", fg="white", text="Q11", font=myfont, anchor=W)
    q11.place(relwidth=0.2, relheight=rh, rely=(5*x)+(6*h))
    
    global mon10
    global q10
    mon10 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m10, font=myfont, anchor=E)
    mon10.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(6*x)+(7*h))
    q10 = Label(ecanv, bg="#5B0A91", fg="white", text="Q10", font=myfont, anchor=W)
    q10.place(relwidth=0.2, relheight=rh, rely=(6*x)+(7*h))
    
    global mon9
    global q9
    mon9 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m9, font=myfont, anchor=E)
    mon9.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(7*x)+(8*h))
    q9 = Label(ecanv, bg="#5B0A91", fg="white", text="Q9", font=myfont, anchor=W)
    q9.place(relwidth=0.2, relheight=rh, rely=(7*x)+(8*h))
    
    global mon8
    global q8
    mon8 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m8, font=myfont, anchor=E)
    mon8.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(8*x)+(9*h))
    q8 = Label(ecanv, bg="#5B0A91", fg="white", text="Q8", font=myfont, anchor=W)
    q8.place(relwidth=0.2, relheight=rh, rely=(8*x)+(9*h))
    
    global mon7
    global q7
    mon7 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m7, font=myfont, anchor=E)
    mon7.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(9*x)+(10*h))
    q7 = Label(ecanv, bg="#5B0A91", fg="white", text="Q7", font=myfont, anchor=W)
    q7.place(relwidth=0.2, relheight=rh, rely=(9*x)+(10*h))
    
    global mon6
    global q6
    mon6 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m6, font=myfont, anchor=E)
    mon6.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(10*x)+(11*h))
    q6 = Label(ecanv, bg="#5B0A91", fg="white", text="Q6", font=myfont, anchor=W)
    q6.place(relwidth=0.2, relheight=rh, rely=(10*x)+(11*h))
    
    global mon5
    global q5
    mon5 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m5, font=myfont, anchor=E)
    mon5.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(11*x)+(12*h))
    q5 = Label(ecanv, bg="#5B0A91", fg="white", text="Q5", font=myfont, anchor=W)
    q5.place(relwidth=0.2, relheight=rh, rely=(11*x)+(12*h))
    
    global mon4
    global q4
    mon4 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m4, font=myfont, anchor=E)
    mon4.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(12*x)+(13*h))
    q4 = Label(ecanv, bg="#5B0A91", fg="white", text="Q4", font=myfont, anchor=W)
    q4.place(relwidth=0.2, relheight=rh, rely=(12*x)+(13*h))
    
    global mon3
    global q3
    mon3 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m3, font=myfont, anchor=E)
    mon3.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(13*x)+(14*h))
    q3 = Label(ecanv, bg="#5B0A91", fg="white", text="Q3", font=myfont, anchor=W)
    q3.place(relwidth=0.2, relheight=rh, rely=(13*x)+(14*h))
    
    global mon2
    global q2
    mon2 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m2, font=myfont, anchor=E)
    mon2.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(14*x)+(15*h))
    q2 = Label(ecanv, bg="#5B0A91", fg="white", text="Q2", font=myfont, anchor=W)
    q2.place(relwidth=0.2, relheight=rh, rely=(14*x)+(15*h))

    global mon1
    global q1
    mon1 = Label(ecanv, bg="#5B0A91", fg="white", text="₹"+m1, font=myfont, anchor=E)
    mon1.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(15*x)+(16*h))
    q1 = Label(ecanv, bg="#5B0A91", fg="white", text="Q1", font=myfont, anchor=W)
    q1.place(relwidth=0.2, relheight=rh, rely=(15*x)+(16*h))


    #RIVIVAL
    #FRAME FOR BORDER
    global revbox                                                      #SKIN FRAME RIGID
    revbox = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    revbox.place(relwidth=0.19, relheight=0.1, relx=0.74, rely=0.76)     
    global revboxppl                                                    #PURPLE FRAME
    revboxppl = Frame(revbox, bg="#5B0A91")
    revboxppl.place(relwidth=1, relheight=1)
    global rimg                                                         #LABELS ON "reboxppl" FRAME
    global l1                                                           #INDICATES NUMBER OF REVIVALS LEFT
    global l2                                                           #BY FILLED HEARTS
    global l3
    pathg=".\img\ill.png"
    kl = Image.open(pathg)
    kl = kl.resize((50, 50), Image.ANTIALIAS)
    rimg = ImageTk.PhotoImage(kl)
    l1 = Label(revboxppl, image=rimg, bg="#5B0A91")
    l1.place(relheight=1, relwidth=0.3)
    l2 = Label(revboxppl, image=rimg, bg="#5B0A91")
    l2.place(relheight=1, relwidth=0.3, relx=0.345)
    l3 = Label(revboxppl, image=rimg, bg="#5B0A91")
    l3.place(relheight=1, relwidth=0.3, relx=0.696)


    #REVIVE BUTTON
    global rbut
    global revive
    revive = Frame(root, bg="green", bd=10, relief="ridge")
    revive.place(relwidth=0.06334, relheight=0.08, relx=0.73, rely=0.88)
    rbut = Button(revive, bg="#5B0A91", fg="white", font=myfont, text="REVIVE", state=DISABLED)
    rbut.place(relwidth=1, relheight=1)


    #QUIT BUTTON
    global quit
    global qbut
    quit = Frame(root, bg="red", bd=10, relief="ridge")
    quit.place(relwidth=0.05334, relheight=0.08, relx=0.80334, rely=0.88)
    qbut = Button(quit, bg="#5B0A91", fg="white", font=myfont, text="QUIT", command=QUIT)
    qbut.place(relwidth=1, relheight=1)


    #NEXT BUTTON
    global nxt
    global nbut
    nxt = Frame(root, bg="yellow", bd=10, relief="ridge")
    nxt.place(relwidth=0.07334, relheight=0.08, relx=0.86668, rely=0.88)
    nbut = Button(nxt, bg="#5B0A91", fg="white", font=myfont, text="NEXT", state=DISABLED)
    nbut.place(relwidth=1, relheight=1)



                                                                        #-------------------------------
    #-------------------------------------------------------------------#||INSTRUCTIONS TO FOLLOW PAGE||-------------------------------------------------------------------#
                                                                        #-------------------------------
    global funcstart
    funcstart = Frame(root, bg="#C5B358", bd=10, relief="ridge")     #AFTER THE WHOLE PANEL IS DEFINED THE '''funcstart''' HIDES EVERYTHING
    funcstart.place(relwidth=0.9, relheight=0.95, relx=0.05, rely=0.025)  #AND THUS MAKES IT LOOK LIKE THE RULES AND REGULATIONS PAGE WAS DEFINED BEFORE THE MAIN PANEL

    #INSTRUCTIONS TO FOLLOW
    instFR = Label(funcstart, bg="#C5B358", bd=10, relief="ridge")
    instFR.place(relwidth=0.5, relheight=0.12, relx=0.02, rely=0.06)
    inst = Label(instFR, bg="#5B0A91", fg="white", text="RULES AND REGULATIONDS :-", font=myfontH)     #PAGE HEADING
    inst.place(relwidth=1, relheight=1)

    
    instC1 = Text(funcstart, bg="#C5B358",  font=myfont, relief="flat")
    instC1.place(relwidth=0.55, relheight=0.5, relx=0.02, rely=0.26)
    instC1.insert(1.0, "<1> There is NO TIME LIMIT for any of the question\n\n")
    instC1.insert(END, "<2> The Contestent will be offered to tackle INSCREASINGLY DIFFICULT\n       QUESTIONS\n\n")
    instC1.insert(END, "<3> The amount offered is increased simultaniously from ₹1,000 upto ₹7 CRORE\n\n")
    instC1.insert(END, "<4> There are two safety nets on Q5 and Q10 at ₹10,000 and ₹3,20,000                     respectively\n\n")      #GUIDELINES TO FOLLOW
    instC1.insert(END, "<5> The Contestent is provided with 3 REVIVAL LIFELINES\n\n")
    instC1.insert(END, "<6> The LIFELINE REVIVAL simply just SKIPS the question and\n")
    instC1.insert(END, "        moves on to the next question. But use it carefully\n\n")
    instC1.insert(END, "<7> The Contestent can QUIT the game whenever they want and cash out \n        the money they have won\n\n")


    myfont = f.Font(family='Maiandra GD', size=10)
    RBinst = Label(funcstart, bg="#C5B358", font=myfont, text="Revival lifeline can be used by pressing the \nrevive button on left of the COMPUTER SCREEN :")
    RBinst.place(relwidth=0.25, relheight=0.11, relx=0.02, rely=0.85)
    RBexampFR = Frame(funcstart, bg="green", bd=10, relief="ridge")
    RBexampFR.place(relwidth=0.07, relheight=0.11, relx=0.28, rely=0.85)                        #BUTTON EXPL
    myfont = f.Font(family='Maiandra GD', size=15)
    RBexamp = Button(RBexampFR, bg="#5B0A91", fg="white", font=myfont, text="REVIVE")
    RBexamp.place(relwidth=1, relheight=1)


    myfont = f.Font(family='Maiandra GD', size=10)
    QBinst = Label(funcstart, bg="#C5B358", font=myfont, text="The Contestent can quit the game by pressing the\nquit button on left of the COMPUTER SCREEN :")
    QBinst.place(relwidth=0.25, relheight=0.11, relx=0.45, rely=0.85)
    QBexampFR = Frame(funcstart, bg="red", bd=10, relief="ridge")
    QBexampFR.place(relwidth=0.07, relheight=0.11, relx=0.71, rely=0.85)                        #BUTTON EXPL
    myfont = f.Font(family='Maiandra GD', size=15)
    QBexamp = Button(QBexampFR, bg="#5B0A91", fg="white", font=myfont, text="QUIT")
    QBexamp.place(relwidth=1, relheight=1)


    qlistINT = Frame(funcstart, bg="#C5B358", bd=10, relief="ridge")
    qlistINT.place(relx=0.6, rely=0.06, relwidth=0.35, relheight=0.74)
    ecanvINT = Canvas(qlistINT)
    ecanvINT.place(relwidth=1, relheight=1)
    x=0.060375
    h=0.002
    rh=0.0595
    myfont = f.Font(family='Maiandra GD', weight="bold")
    
    m16 = "7 CRORE" 
    m15 = "1 CRORE" 
    m14 = "50,00,000"
    m13 = "25,00,000"
    m12 = "12,50,000"
    m11 = "6,40,000"
    m10 = "3,20,000"
    m9 = "1,60,000"
    m8 = "80,000"  
    m7 = "40,000"  
    m6 = "20,000"  
    m5 = "10,000"  
    m4 = "5,000"   
    m3 = "3,000"   
    m2 = "2,000"
    m1 = "1,000" 
    

    money16 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m16, font=myfont, anchor=E)
    money16.place(relwidth=0.8, relx=0.2, relheight=rh, rely=h)
    que16 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q16", font=myfont, anchor=W)
    que16.place(relwidth=0.2, relheight=rh, rely=h)
    money16.after(6400, lambda: money16.configure(bg="yellow", fg="black"))
    que16.after(6400, lambda: que16.configure(bg="yellow", fg="black"))
    money16.after(6800, lambda: money16.configure(bg="#5B0A91", fg="white"))                         #FLASHING ALL QUESTION NO.S ON LIST
    que16.after(6800, lambda: que16.configure(bg="#5B0A91", fg="white"))                               #ONE AFTER THE OTHER
    
    money15 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m15, font=myfont, anchor=E)
    money15.place(relwidth=0.8, relx=0.2, relheight=rh, rely=x+h+h)
    que15 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q15", font=myfont, anchor=W)
    que15.place(relwidth=0.2, relheight=rh, rely=x+h+h)
    money15.after(6000, lambda: money15.configure(bg="yellow", fg="black"))
    que15.after(6000, lambda: que15.configure(bg="yellow", fg="black"))
    money15.after(6400, lambda: money15.configure(bg="#5B0A91", fg="white"))
    que15.after(6400, lambda: que15.configure(bg="#5B0A91", fg="white"))
    
    money14 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m14, font=myfont, anchor=E)
    money14.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(2*x)+(3*h))
    que14 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q14", font=myfont, anchor=W)
    que14.place(relwidth=0.2, relheight=rh, rely=(2*x)+(3*h))
    money14.after(5600, lambda: money14.configure(bg="yellow", fg="black"))
    que14.after(5600, lambda: que14.configure(bg="yellow", fg="black"))
    money14.after(6000, lambda: money14.configure(bg="#5B0A91", fg="white"))
    que14.after(6000, lambda: que14.configure(bg="#5B0A91", fg="white"))
    
    money13 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m13, font=myfont, anchor=E)
    money13.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(3*x)+(4*h))
    que13 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q13", font=myfont, anchor=W)
    que13.place(relwidth=0.2, relheight=rh, rely=(3*x)+(4*h))
    money13.after(5200, lambda: money13.configure(bg="yellow", fg="black"))
    que13.after(5200, lambda: que13.configure(bg="yellow", fg="black"))
    money13.after(5600, lambda: money13.configure(bg="#5B0A91", fg="white"))
    que13.after(5600, lambda: que13.configure(bg="#5B0A91", fg="white"))
    
    money12 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m12, font=myfont, anchor=E)
    money12.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(4*x)+(5*h))
    que12 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q12", font=myfont, anchor=W)
    que12.place(relwidth=0.2, relheight=rh, rely=(4*x)+(5*h))
    money12.after(4800, lambda: money12.configure(bg="yellow", fg="black"))
    que12.after(4800, lambda: que12.configure(bg="yellow", fg="black"))
    money12.after(5200, lambda: money12.configure(bg="#5B0A91", fg="white"))
    que12.after(5200, lambda: que12.configure(bg="#5B0A91", fg="white"))
    
    money11 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m11, font=myfont, anchor=E)
    money11.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(5*x)+(6*h))
    que11 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q11", font=myfont, anchor=W)
    que11.place(relwidth=0.2, relheight=rh, rely=(5*x)+(6*h))
    money11.after(4400, lambda: money11.configure(bg="yellow", fg="black"))
    que11.after(4400, lambda: que11.configure(bg="yellow", fg="black"))
    money11.after(4800, lambda: money11.configure(bg="#5B0A91", fg="white"))
    que11.after(4800, lambda: que11.configure(bg="#5B0A91", fg="white"))
    
    money10 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m10, font=myfont, anchor=E)
    money10.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(6*x)+(7*h))
    que10 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q10", font=myfont, anchor=W)
    que10.place(relwidth=0.2, relheight=rh, rely=(6*x)+(7*h))
    money10.after(4000, lambda: money10.configure(bg="yellow", fg="black"))
    que10.after(4000, lambda: que10.configure(bg="yellow", fg="black"))
    
    money9 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m9, font=myfont, anchor=E)
    money9.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(7*x)+(8*h))
    que9 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q9", font=myfont, anchor=W)
    que9.place(relwidth=0.2, relheight=rh, rely=(7*x)+(8*h))
    money9.after(3600, lambda: money9.configure(bg="yellow", fg="black"))
    que9.after(3600, lambda: que9.configure(bg="yellow", fg="black"))
    money9.after(4000, lambda: money9.configure(bg="#5B0A91", fg="white"))
    que9.after(4000, lambda: que9.configure(bg="#5B0A91", fg="white"))
    
    money8 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m8, font=myfont, anchor=E)
    money8.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(8*x)+(9*h))
    que8 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q8", font=myfont, anchor=W)
    que8.place(relwidth=0.2, relheight=rh, rely=(8*x)+(9*h))
    money8.after(3200, lambda: money8.configure(bg="yellow", fg="black"))
    que8.after(3200, lambda: que8.configure(bg="yellow", fg="black"))
    money8.after(3600, lambda: money8.configure(bg="#5B0A91", fg="white"))
    que8.after(3600, lambda: que8.configure(bg="#5B0A91", fg="white"))
    
    money7 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m7, font=myfont, anchor=E)
    money7.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(9*x)+(10*h))
    que7 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q7", font=myfont, anchor=W)
    que7.place(relwidth=0.2, relheight=rh, rely=(9*x)+(10*h))
    money7.after(2800, lambda: money7.configure(bg="yellow", fg="black"))
    que7.after(2800, lambda: que7.configure(bg="yellow", fg="black"))
    money7.after(3200, lambda: money7.configure(bg="#5B0A91", fg="white"))
    que7.after(3200, lambda: que7.configure(bg="#5B0A91", fg="white"))
    
    money6 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m6, font=myfont, anchor=E)
    money6.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(10*x)+(11*h))
    que6 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q6", font=myfont, anchor=W)
    que6.place(relwidth=0.2, relheight=rh, rely=(10*x)+(11*h))
    money6.after(2400, lambda: money6.configure(bg="yellow", fg="black"))
    que6.after(2400, lambda: que6.configure(bg="yellow", fg="black"))
    money6.after(2800, lambda: money6.configure(bg="#5B0A91", fg="white"))
    que6.after(2800, lambda: que6.configure(bg="#5B0A91", fg="white"))
    
    money5 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m5, font=myfont, anchor=E)
    money5.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(11*x)+(12*h))
    que5 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q5", font=myfont, anchor=W)
    que5.place(relwidth=0.2, relheight=rh, rely=(11*x)+(12*h))
    money5.after(2000, lambda: money5.configure(bg="yellow", fg="black"))
    que5.after(2000, lambda: que5.configure(bg="yellow", fg="black"))
    
    money4 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m4, font=myfont, anchor=E)
    money4.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(12*x)+(13*h))
    que4 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q4", font=myfont, anchor=W)
    que4.place(relwidth=0.2, relheight=rh, rely=(12*x)+(13*h))
    money4.after(1600, lambda: money4.configure(bg="yellow", fg="black"))
    que4.after(1600, lambda: que4.configure(bg="yellow", fg="black"))
    money4.after(2000, lambda: money4.configure(bg="#5B0A91", fg="white"))
    que4.after(2000, lambda: que4.configure(bg="#5B0A91", fg="white"))
    
    money3 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m3, font=myfont, anchor=E)
    money3.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(13*x)+(14*h))
    que3 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q3", font=myfont, anchor=W)
    que3.place(relwidth=0.2, relheight=rh, rely=(13*x)+(14*h))
    money3.after(1200, lambda: money3.configure(bg="yellow", fg="black"))
    que3.after(1200, lambda: que3.configure(bg="yellow", fg="black"))
    money3.after(1600, lambda: money3.configure(bg="#5B0A91", fg="white"))
    que3.after(1600, lambda: que3.configure(bg="#5B0A91", fg="white"))
    
    money2 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m2, font=myfont, anchor=E)
    money2.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(14*x)+(15*h))
    que2 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q2", font=myfont, anchor=W)
    que2.place(relwidth=0.2, relheight=rh, rely=(14*x)+(15*h))
    money2.after(800, lambda: money2.configure(bg="yellow", fg="black"))
    que2.after(800, lambda: que2.configure(bg="yellow", fg="black"))
    money2.after(1200, lambda: money2.configure(bg="#5B0A91", fg="white"))
    que2.after(1200, lambda: que2.configure(bg="#5B0A91", fg="white"))

    money1 = Label(ecanvINT, bg="#5B0A91", fg="white", text="₹"+m1, font=myfont, anchor=E)
    money1.place(relwidth=0.8, relx=0.2, relheight=rh, rely=(15*x)+(16*h))
    que1 = Label(ecanvINT, bg="#5B0A91", fg="white", text="Q1", font=myfont, anchor=W)
    que1.place(relwidth=0.2, relheight=rh, rely=(15*x)+(16*h))
    money1.after(400, lambda: money1.configure(bg="yellow", fg="black"))
    que1.after(400, lambda: que1.configure(bg="yellow", fg="black"))
    money1.after(800, lambda: money1.configure(bg="#5B0A91", fg="white"))
    que1.after(800, lambda: que1.configure(bg="#5B0A91", fg="white"))
    


    start = Button(funcstart, bg="#C5B358", font=myfont, command=functioning, text="START -->")
    start.place(relwidth=0.1, relheight=0.1, relx=0.86, rely=0.85)





#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#
#  OOOOOOOOO   PPPPPPP    TTTTTTT
#  O       O   P     P       T
#  O       O   P     P       T
#  O       O   PPPPPPP       T
#  O       O   P             T
#  O       O   P             T
#  OOOOOOOOO   P             T
#
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
def OPTIONA():
    winsound.PlaySound('btn.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    global option
    global optionW
    dispopt.delete(0, END)
    dispopt.insert(0, OPTA)
    option = "a"                                                                    #To tell that OPTION "a" has been chosen
    optionW = OPTA                                                                   #stores content of OPTION "a"
    lockb.configure(state=ACTIVE, command=LOCKconf, bg="#5B0A91", fg="white")

def OPTIONB():
    winsound.PlaySound('btn.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    global option
    global optionW
    dispopt.delete(0, END)
    dispopt.insert(0, OPTB)
    option = "b"                                                                   #To tell that OPTION "b" has been chosen
    optionW = OPTB                                                                  #stores content of OPTION "b"
    lockb.configure(state=ACTIVE, command=LOCKconf, bg="#5B0A91", fg="white")

def OPTIONC():
    winsound.PlaySound('btn.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    global option
    global optionW
    dispopt.delete(0, END)
    dispopt.insert(0, OPTC)
    option = "c"                                                                    #To tell that OPTION "c" has been chosen
    optionW = OPTC                                                                  #stores content of OPTION "c"
    lockb.configure(state=ACTIVE, command=LOCKconf, bg="#5B0A91", fg="white")
    
def OPTIOND():
    winsound.PlaySound('btn.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    global option
    global optionW
    dispopt.delete(0, END)
    dispopt.insert(0, OPTD)
    option = "d"                                                                  #To tell that OPTION "d" has been chosen
    optionW = OPTD                                                                  #stores content of OPTION "d"
    lockb.configure(state=ACTIVE, command=LOCKconf, bg="#5B0A91", fg="white")







#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#
#   L            OOOOOOOOO    CCCCCCCC   K     K
#   L            O       O    C          K   K
#   L            O       O    C          K  K 
#   L            O       O    C          K K
#   L            O       O    C          K  K
#   L            O       O    C          K   K
#   L            O       O    C          K     K
#   LLLLLLLLLL   OOOOOOOOO    CCCCCCCC   K       K
#
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
def LOCKconf():	
    winsound.PlaySound('btn.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)          #BTN SOUND
    myfont = f.Font(family='Maiandra GD')                                          #DEFINED FONT

    global lockBG
    lockBG = Label(root, bg="#C5B358")                                              #POPUP BACKGROUND PURPLE
    lockBG.place(relwidth=1, relheight=1)
    lockFR = Frame(lockBG, bg="#C5B358", bd=10, relief="ridge")                       #POPUP FRAME CREME
    lockFR.place(relwidth=0.7, relheight=0.35, relx=0.5, rely=0.23, anchor='n')
    lockPOP = Label(lockFR, bg="#5B0A91", fg="white", font=myfont, text="Are you sure you want to lock option ["+option+"] "+str(optionW))
    lockPOP.place(relwidth=1, relheight=1)                                          #POPUP CONTENT

    #YES
    global yesFR
    yesFR = Frame(root, bg="#C5B358", bd=10, relief="ridge")                                  #YES FRAME
    yesFR.place(relx=0.2, rely=0.6, relwidth=0.15, relheight=0.08)    
    yes = Button(yesFR, bg="#5B0A91", fg="white", font=myfont, text="YES", command=LOCK)      #YES BUTTON
    yes.place(relwidth=1, relheight=1)

    #NO
    global noFR
    noFR = Frame(root, bg="#C5B358", bd=10, relief="ridge")                                   #NO FRAME
    noFR.place(relx=0.65, rely=0.6, relwidth=0.15, relheight=0.08)
    no = Button(noFR, bg="#5B0A91", fg="white", font=myfont, text="NO", command=lockno)       #NO BUTTON
    no.place(relwidth=1, relheight=1)

def lockno():
    winsound.PlaySound('btn.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    lockBG.place_forget() 
    yesFR.place_forget()                                                                      #POPUP GETS REMOVED
    noFR.place_forget()                                                                       #BACK TO SELECTING OPTIONS

def LOCK():
    winsound.PlaySound('btn.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    if number>=10 and number<=16:
        lockBG.after(240, lambda: winsound.PlaySound('KBC TNSN F.wav', winsound.SND_ALIAS | winsound.SND_ASYNC))
    else:
        lockBG.after(240, lambda: winsound.PlaySound('KBC TNSN.wav', winsound.SND_ALIAS | winsound.SND_ASYNC))

    lockBG.place_forget()
    yesFR.place_forget()                                                                      #POPUP GETS REMOVED
    noFR.place_forget()

    BA.configure(state=DISABLED)
    BB.configure(state=DISABLED)
    BC.configure(state=DISABLED)                                                          #DISABLE/ENABLE OPTION AND LOCK BUTTON
    BD.configure(state=DISABLED)
    lockb.configure(state=DISABLED)
    confb.configure(state=NORMAL, command=CONFIRM, bg="yellow", fg="black")
    qbut.configure(state=DISABLED)

    if rev==0 or rev<0:
        rbut.configure(state=DISABLED, bg="#5B0A91", fg="white")                                       #IF REVIVE LIFELINES ARE ZERO
    else:
        rbut.configure(state=NORMAL, command=REVIVE, bg="yellow", fg="black")                     #ELSE ENABLE REVIVE BUTTON



    if option == "a":
        BA.configure(bg="grey", fg="white")
        OA.configure(bg="grey", fg="white")                                                  #GREY ON CHOSEN OPTION
    if option == "b":
        BB.configure(bg="grey", fg="white")
        OB.configure(bg="grey", fg="white")
    if option == "c":
        BC.configure(bg="grey", fg="white")
        OC.configure(bg="grey", fg="white")
    if option == "d":
        BD.configure(bg="grey", fg="white")
        OD.configure(bg="grey", fg="white")
    



#Ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#
#    CCCCCCCC    OOOOOOOOO    NN        N    FFFFFFFFFF
#    C           O       O    N N       N    F
#    C           O       O    N  N      N    F
#    C           O       O    N   N     N    FFFFFFFFF
#    C           O       O    N    N    N    F
#    C           O       O    N     N   N    F
#    C           O       O    N      N  N    F
#    CCCCCCCC    OOOOOOOOO    N       N N    F
#   
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
def CONFIRM():
    global nbut                                               #TO ENABLE NEXT BUTTON WHEN CONFIRM IS CLICKED
    myfontH = f.Font(family='Maiandra GD', size=30)           #DEFINED FONT FOR CONFIRM
    bigfont = f.Font(family='Maiandra GD', size=20)
    rbut.configure(state=DISABLED, bg="#5B0A91", fg="white")
    confb.configure(state=DISABLED, bg="#5B0A91", fg="white")

    global agla
    if number==16:
        agla = "NAHI"
    if number==15:
        agla = "Sollvey" 
    if number==14:
        agla = "Pandrhawe"
    if number==13:
        agla = "Chodwe"
    if number==12:
        agla = "Terwe"
    if number==11:
        agla = "Barwe"
    if number==10:
        agla = "Gyarwe"
    if number==9:
        agla = "Daswe"
    if number==8:
        agla = "Nawe"
    if number==7:
        agla = "Aathwe"
    if number==6:
        agla = "Satwe"
    if number==5:
        agla = "Chhate"
    if number==4:
        agla = "Panchwe"
    if number==3:
        agla = "Chothe"
    if number==2:
        agla = "Teesre"
    if number==1:
        agla = "Dusre"

    global checkp                     #AMOUNT WON BY THE USER(1-1000   2-2000   3-3000   4-5000)
    global checkpLBD
    if number>0 and number<=5:         #CHECKPOINT AMOUNT - SAFTYNET-0
        checkp = "0"
        checkpLBD = "0"
    if number>5 and number<=10:         #CHECKPOINT AMOUNT - SAFTYNET-1
        checkp = "10,000"
        checkpLBD = "10000"
    if number>10 and number<=16:         #CHECKPOINT AMOUNT - SAFTYNET-2
        checkp = "3,20,000"
        checkpLBD = "320000"


    global won                              #VARIABLE THAT STORES THE FINAL AMOUNT TAKEN BY USER
    global wonlbd

    if ANSO == option:        #and number!=16                                      #CORRECT
        winsound.PlaySound('CORR1.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

        corr = Frame(root, bg="grey", bd=10, relief="ridge")
        corr.place(relwidth=0.25, relheight=0.2, relx=0.06, rely=0.76)
        myfont = f.Font(family='Maiandra GD', size=46, weight="bold")               #DEFINING CORRECTION ENTRY AGAIN - GREEN
        ecorr = Entry(corr, bg="green", fg="white", font=myfont)
        ecorr.place(relwidth=1, relheight=1)
        
        ecorr.delete(0, END)
        ecorr.insert(0, "  CORECT")
        tact.configure(font=bigfont)
        tact.delete(1.0, END)
        apric = ["You won ₹{}".format(curr),"You have won ₹{}".format(curr)]
        tact.insert(1.0, "\n"+random.choice(apric)+" \n")
        if number==16:
            tact.insert(END, "CONGRATULATIONS!!")
        else:
            tact.insert(END, "badte hai "+agla+" prashna ki or")

        won = curr                                                               #SETTING WON TO THE CURRENTLY WON AMOUNT
        wonlbd = currlbd
        
        moneye.delete(0, END)
        moneye.insert(0, won)                                                    #DISPLAYING CURRENTLY WON AMOUNT


        if option == "a":
            BA.configure(bg="green", fg="white")
            OA.configure(bg="green", fg="white")                                                  #green ON CHOSEN OPTION
        if option == "b":
            BB.configure(bg="green", fg="white")
            OB.configure(bg="green", fg="white")
        if option == "c":
            BC.configure(bg="green", fg="white")
            OC.configure(bg="green", fg="white")
        if option == "d":
            BD.configure(bg="green", fg="white")
            OD.configure(bg="green", fg="white")

        if number==16:
            nbut.configure(text="END", state=NORMAL, command=appr)                         #TAKES TO THE APPR PANEL
        else:
            nbut.configure(state=NORMAL, command=functioning)                        #TO THE NEXT QUESTION



    else:                                  #WRONG

        winsound.PlaySound('KBC WRNG ANS.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)


        if option == "a":
            BA.configure(bg="red", fg="white")
            OA.configure(bg="red", fg="white")                                                  #red ON WRONG OPTION
        if option == "b":
            BB.configure(bg="red", fg="white")
            OB.configure(bg="red", fg="white")
        if option == "c":
            BC.configure(bg="red", fg="white")
            OC.configure(bg="red", fg="white")
        if option == "d":
            BD.configure(bg="red", fg="white")
            OD.configure(bg="red", fg="white")


        if ANSO == "a":
            BA.configure(bg="green", fg="white")
            OA.configure(bg="green", fg="white")                                                  #green ON THE ACTUAL CORRECT AMSWER 
        if ANSO == "b":
            BB.configure(bg="green", fg="white")
            OB.configure(bg="green", fg="white")
        if ANSO == "c":
            BC.configure(bg="green", fg="white")
            OC.configure(bg="green", fg="white")
        if ANSO == "d":
            BD.configure(bg="green", fg="white")
            OD.configure(bg="green", fg="white")

        corr = Frame(root, bg="red", bd=15, relief="ridge")
        corr.place(relwidth=0.25, relheight=0.2, relx=0.06, rely=0.76)
        myfont = f.Font(family='Maiandra GD', size=46, weight="bold")
        ecorr = Entry(corr, bg="red", fg="white", font=myfont)
        ecorr.place(relwidth=1, relheight=1)
        ecorr.delete(0, END)
        ecorr.insert(0, "  WRONG")

        myfont = f.Font(family='Maiandra GD')
        tact.configure(font=myfont)
        tact.delete(1.0, END)
        tact.insert(1.0, "SORRY "+name+"ji AAPKA SAFAR YAHI KHATAM HOTA HAI\nTHE CORRECT ANSWER WAS\nOption ["+ANSO+"] "+ANSW+"\n")
        tact.insert(END, "\nTo ye the "+state+" ke "+name+" ji\n jeet kar gaye ₹"+checkp+" rupay")

        won = checkp
        wonlbd = checkpLBD

        moneye.delete(0, END)
        moneye.insert(0, won)

        nbut.configure(text="END",state=NORMAL, command=LEADERBOARD)                           #TAKES TO THE LEADERBOARD

        #BUTTON LEADING TO APPR






#Ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#    QQQQQQQQQQQ                        AAAAAAAAA     PPPPPPPPPP      PPPPPPPPPP     
#    QQQ     QQQ                        AAAAAAAAA     PPPPPPPPPPP     PPPPPPPPPPP    
#    QQQ     QQQ                        AAA   AAA     PPPP      PP    PPPP      PP   
#    QQQ     QQQ                        AAA   AAA     PPPPPPPPPPP     PPPPPPPPPPP    
#    QQQ     QQQ        =========       AAAAAAAAA     PPPPPPPP        PPPPPPPP    
#    QQQ   Q QQQ                        AAA   AAA     PPPP            PPPP        
#    QQQ   QQQQQ                        AAA   AAA     PPPP            PPPP        
#    QQQQQQQQQQQ                        AAA   AAA     PPPP            PPPP        
#            QQQQQQQ                    AAA   AAA     PPPP            PPPP        
#Ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#

def appr():

    path2=".\img\KK3.jpg"
    k2 = Image.open(path2)
    k2 = k2.resize((1400, 800), Image.ANTIALIAS)                         #GOLDEN BACKGROUND IMAGE PATH DEFINATION
    img1 = ImageTk.PhotoImage(k2)


    hfont = f.Font(family='Maiandra GD', size=35)                        #DEFINING FONT FOR THE PAGE
    myfont = f.Font(family='Maiandra GD')

    global funcend
    funcend = Label(root, bg="#C5B358", bd=10, relief="ridge")
    funcend.place(relwidth=0.9, relheight=0.95, relx=0.05, rely=0.025)   #MAKING THE APPR PAGE AND PUTTING IT ON SCREEN
    funcend.configure(image=img1)
    funcend.image = img1




    #YOUWON
    labelWONfr = Frame(funcend, bg="#C5B358", bd=10, relief="ridge")
    labelWONfr.place(relwidth=0.7, relheight=0.25, relx=0.15, rely=0.04)
    labelWON = Button(labelWONfr, bg="#5B0A91", fg="white", font=hfont, text="YOU WON")               #PAGE HEADER SAYING "YOU WON"
    labelWON.place(relwidth=1, relheight=1)





    path3=".\img\chk4.jpg"
    k3 = Image.open(path3)
    k3 = k3.resize((600, 275), Image.ANTIALIAS)                                                     #DEFINING IMAGE PATH FOR THE CHECK
    img2 = ImageTk.PhotoImage(k3)

    checkF = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    checkF.place(relx=0.24, rely=0.35, relheight=0.380, relwidth=0.510)
    check = Label(checkF)                                                                           #MAKING CHECK AND PUTTING IT ON SCREEN
    check.place(relwidth=1, relheight=1)
    check.configure(image=img2)
    check.image = img2



    currdate = list(today.strftime("%d %m %Y"))
    l = []
    for i in currdate:
        l.append(i)
        l.append("  ")                                                                             #STORING CURRENT DATE IN NEW VARIABLE
    l = "".join(l)
    cname = Label(checkF, text=name, bg="#FFFFFF").place(relx=0.15,rely=0.18)                    #NAME
    crupe = Label(checkF, text="7 CRORE only /-", bg="#FFFFFF").place(relx=0.2, rely=0.3)          #RUPEES IN WORDS
    crupn = Label(checkF, text=wonlbd, bg="#FFFFFF").place(relx=0.8, rely=0.43)                     #RUPEES IN NUMBERS
    cdate = Label(checkF, text=l, bg="#FFFFFF").place(relx=0.75, rely=0.05)                      #DATE



    moneyf = Frame(funcend, bg="#C5B358", bd=10, relief="ridge")
    moneyf.place(relx = 0.25, rely=0.8,relwidth=0.5,relheight=0.1)
    rup = Label(moneyf, bg="#5B0A91", fg="white", font=myfont, relief="raised", text="₹")          #MONEY BAR 
    rup.place(relx=0.015, rely=0.04, relwidth=0.3, relheight=0.85)
    moneye = Entry(moneyf, bg="white", font=myfont,relief="sunken")
    moneye.place(relx=0.35, rely=0.04, relwidth=0.635, relheight=0.85)
    moneye.insert(0, won)



    ldframe = Frame(funcend, bg="#C5B358", bd=10, relief="ridge")
    ldframe.place(relx=0.8, rely=0.85, relwidth=0.15, relheight=0.1)                                                  #LEADERBOARD BUTTON
    ldbutton = Button(ldframe, bg="#5B0A91", fg="#ffffff", font=myfont , text="LEADERBOARD", command=LEADERBOARD)
    ldbutton.place(relwidth=1,relheight=1)





#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#
#    FFFFFFFFFFFFFFFFF      U             U      NN            N       CCCCCCCCCCCCCC
#    FFFFFFFFFFFFFFFFF      U             U      N N           N       C
#    FF                     U             U      N  N          N       C
#    FF                     U             U      N   N         N       C
#    FFFFFFFFFFFFF          U             U      N    N        N       C
#    FFFFFFFFFFFFF          U             U      N     N       N       C
#    FF                     U             U      N      N      N       C
#    FF                     U             U      N       N     N       C
#    FF                     U             U      N        N    N       C
#    FF                     U             U      N         N   N       C
#    FF                     U             U      N          N  N       C
#    FF                      U           U       N           N N       C
#    FF                       UUUUUUUUUUU        N            NN       CCCCCCCCCCCCCCCC
#
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
p=random.sample(range(1,11),5)   #5 UNIQUE RANDOM NUMBERS
number=0
def functioning():
    kpl = 0 
    i = 1
    de = 150

    #NEXT BUTTON SOUND
    winsound.PlaySound('btn.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)


    #AFTER FIRST ITERATION TO SET THE CHANGES BACK TO NORMAL-------------------
    OA.configure(bg="#C5B358", fg="black")
    OB.configure(bg="#C5B358", fg="black")
    OC.configure(bg="#C5B358", fg="black")   
    OD.configure(bg="#C5B358", fg="black")
    lockb.configure(state=DISABLED)
    funcstart.place_forget()
    BA.configure(state=NORMAL, command=OPTIONA, bg="#5B0A91", fg="white")                #RESTORING ALL CHANGES TO DEFAULT AFTER A QUESTION
    BB.configure(state=NORMAL, command=OPTIONB, bg="#5B0A91", fg="white")
    BC.configure(state=NORMAL, command=OPTIONC, bg="#5B0A91", fg="white")
    BD.configure(state=NORMAL, command=OPTIOND, bg="#5B0A91", fg="white")
    rbut.configure(state=DISABLED, bg="#5B0A91", fg="#ffffff")
    confb.configure(state=DISABLED, bg="#5B0A91", fg="#ffffff")
    nbut.configure(state=DISABLED)
    qbut.configure(state=NORMAL, command=QUIT)

    global corr
    global ecorr
    corr = Frame(root, bg="grey", bd=10, relief="ridge")
    corr.place(relwidth=0.25, relheight=0.2, relx=0.06, rely=0.76)                #DEFINING CONF BUTTON AGAIN
    myfont = f.Font(family='Maiandra GD', size=46, weight="bold")
    ecorr = Entry(corr, bg="#5B0A91", fg="white", font=myfont)
    ecorr.place(relwidth=1, relheight=1)




    global number                #"number" VARIABLE INDICATES THE QUESTION NUMBER
    global QNO
    number+=1
    print("QNO",number)

    #MYSQL CONNECTION AND IMPORTING CONNECTIONS
    if number==1 or number==6 or number==11:
        QNO=p[0]
    if number==2 or number==7 or number==12:
        QNO=p[1]
    if number==3 or number==8 or number==13:
        QNO=p[2]
    if number==4 or number==9 or number==14:
        QNO=p[3]
    if number==5 or number==10 or number==15:
        QNO=p[4]
    if number==16:
        QNO=p[2]

    global OPTA
    global OPTB
    global OPTC
    global OPTD
    global ANSW
    global ANSO
    if number>0 and number<=5:
        mycursor.execute('select * from hhE where QNO={}'.format(QNO))             #Q1-5 EASY TABLE
        for k in mycursor:
            QUESTION = k[1]
            OPTA = k[2]
            OPTB = k[3]
            OPTC = k[4]
            OPTD = k[5]
            ANSW = k[6]
            ANSO = k[7]
    if number>5 and number<=10:
        mycursor.execute('select * from hhM where QNO={}'.format(QNO))             #Q6-10 MED TABLE
        for k in mycursor:
            QUESTION = k[1]
            OPTA = k[2]
            OPTB = k[3]
            OPTC = k[4]
            OPTD = k[5]
            ANSW = k[6]
            ANSO = k[7]
    if number>10 and number<=15:
        mycursor.execute('select * from hhD where QNO={}'.format(QNO))             #Q11-15 HARD TABLE
        for k in mycursor:
            QUESTION = k[1]
            OPTA = k[2]
            OPTB = k[3]
            OPTC = k[4]
            OPTD = k[5]
            ANSW = k[6]
            ANSO = k[7]
    if number == 16:
        mycursor.execute('select * from hh7 where QNO={}'.format(QNO))             #Q16 7CRORE TABLE
        for k in mycursor:
            QUESTION = k[1]
            OPTA = k[2]
            OPTB = k[3]
            OPTC = k[4]
            OPTD = k[5]
            ANSW = k[6]
            ANSO = k[7]


    global m       #---------    ---------------------    ------------------   #HAVE
    global curr    #---------    ---------------------    ------------------   #TO WIN
    global currlbd
    myfont = f.Font(family='Maiandra GD', weight="bold")
    
    if number==16:
        m = "1 CRORE"  
        curr = "7 CRORE"
        currlbd = "70000000"
        mon16.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q16.configure(bg="yellow", fg="black")
        mon15.configure(bg="#5B0A91", fg="white")
        q15.configure(bg="#5B0A91", fg="white")

        e1.delete(1.0, END)
        e1.insert(1.0, "\nAAKKHIR KAAR ..... wo ghadi aa gayi jiska ham sabko intezaar tha\nEK AAKHRI PRASHN JO AAPKO JITA SAKTA HAI 7 CRORE RUPAY ya neeche la sakta hai seedha ₹3,20,000 par\n")
        e1.insert(END, "TO "+name+" JI AAPKA AAKHRI PRASHNA PURE & CRORE KE LIYEN AAPKI COMPUTER SCREEN PAR .... YE RAHA . . . . .")



    if number==15:
        m = "50,00,000" 
        curr = "1 CRORE"
        currlbd = "10000000" ####################################################################################################################################################
        mon15.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q15.configure(bg="yellow", fg="black")
        mon14.configure(bg="#5B0A91", fg="white")
        q14.configure(bg="#5B0A91", fg="white")

        e1.delete(1.0, END)
        e1.insert(1.0, "\n")
        e1.insert(END, "Bohot unda khel ka pradarshan karte hue "+state+" ke "+name+" jeet chuke hai pure ₹50,000 rupay\n")
        e1.insert(END, "Crorepati ka mukam pane ke bas 2 seedhi door ")
        e1.insert(END, ". To "+name+" JI AAPKA PANDRAWAH PRASHNA PURE \n₹"+curr+" KE LIYE AAPKI COMPUTER SCREEN PAR YEH RAHA...")

    if number==14:
        m = "25,00,000" 
        curr = "50,00,000"
        currlbd = curr.replace(",","")
        mon14.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q14.configure(bg="yellow", fg="black")
        mon13.configure(bg="#5B0A91", fg="white")
        q13.configure(bg="#5B0A91", fg="white")

        e1.delete(1.0, END)
        e1.insert(1.0, "\n")
        e1.insert(END, "  "+name+" ji aapka CHODHWA prashna pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")

    if number==13:
        m = "12,50,000" 
        curr = "25,00,000"
        currlbd = curr.replace(",","")
        mon13.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q13.configure(bg="yellow", fg="black")
        mon12.configure(bg="#5B0A91", fg="white")
        q12.configure(bg="#5B0A91", fg="white")
        
        e1.delete(1.0, END)
        e1.insert(1.0, "\n")
        e1.insert(END, "  "+name+" ji aapka TERHWA prashna pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")
    if number==12:
        m = "6,40,000" 
        curr = "12,50,000"
        currlbd = curr.replace(",","")
        mon12.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q12.configure(bg="yellow", fg="black")
        mon11.configure(bg="#5B0A91", fg="white")
        q11.configure(bg="#5B0A91", fg="white")
        
        e1.delete(1.0, END)
        e1.insert(1.0, "\n")
        e1.insert(END, "  "+name+" ji aapka BARAHWA prashna pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")
    if number==11:
        m = "3,20,000" 
        curr = "6,40,000"
        currlbd = curr.replace(",","")
        mon11.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q11.configure(bg="yellow", fg="black")
        mon10.configure(bg="#5B0A91", fg="white")
        q10.configure(bg="#5B0A91", fg="white")

        e1.delete(1.0, END)
        e1.insert(1.0, "\n")
        e1.insert(END, "  "+name+" ji aapka GYARHWA prashna pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")
    if number==10:
        m = "1,60,000" 
        curr = "3,20,000"
        currlbd = curr.replace(",","")
        mon10.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q10.configure(bg="yellow", fg="black")
        mon9.configure(bg="#5B0A91", fg="white")
        q9.configure(bg="#5B0A91", fg="white")
        
        e1.delete(1.0, END)
        e1.insert(1.0, "  "+name+" aapke safar ke dusre padhaw ka ye aakhri prashna\n")
        e1.insert(END, "Aapko jita sakta hai ₹3,20,000 rupay or yadi aape is prashna ka GHALAT uttar dete hai\n to aap sirf ₹10,000 hi aaj ghar leja payenge\n")
        e1.insert(END, "To "+name+" JI DASWA prashna pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")
    if number==9:
        m = "80,000"   
        curr = "1,60,000"
        currlbd = curr.replace(",","")
        mon9.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q9.configure(bg="yellow", fg="black")
        mon8.configure(bg="#5B0A91", fg="white")
        q8.configure(bg="#5B0A91", fg="white")
        
        e1.delete(1.0, END)
        e1.insert(1.0, "\n")
        e1.insert(END, "  "+name+" ji aapka NAWA prashna pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")
    if number==8:
        m = "40,000"    
        curr = "80,000"
        currlbd = curr.replace(",","")
        mon8.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q8.configure(bg="yellow", fg="black")
        mon7.configure(bg="#5B0A91", fg="white")
        q7.configure(bg="#5B0A91", fg="white")
        
        e1.delete(1.0, END)
        e1.insert(1.0, "\n")
        e1.insert(END, "  "+name+" ji aapka AANTHWA prashna pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")
    if number==7:
        m = "20,000"  
        curr = "40,000"
        currlbd = curr.replace(",","")
        mon7.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q7.configure(bg="yellow", fg="black")
        mon6.configure(bg="#5B0A91", fg="white")
        q6.configure(bg="#5B0A91", fg="white")
        
        e1.delete(1.0, END)
        e1.insert(1.0, "\n")
        e1.insert(END, "  "+name+" ji aapka SAATWA prashna pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")
    if number==6:
        m = "10,000"  
        curr = "20,000"
        currlbd = curr.replace(",","")
        mon6.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q6.configure(bg="yellow", fg="black")
        mon5.configure(bg="#5B0A91", fg="white")
        q5.configure(bg="#5B0A91", fg="white")
        
        e1.delete(1.0, END)
        e1.insert(1.0, "\n")
        e1.insert(END, "  "+name+" ji aapka CHHATA prashna pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")
    if number==5:
        m = "5,000"
        curr = "10,000"
        currlbd = curr.replace(",","")
        mon5.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q5.configure(bg="yellow", fg="black")
        mon4.configure(bg="#5B0A91", fg="white")
        q4.configure(bg="#5B0A91", fg="white")
        
        e1.delete(1.0, END)
        e1.insert(1.0, "\n")
        e1.insert(END, "Aapke pehle padaw ka akhri prashna\n")
        e1.insert(END, "Is prashn ka sahi uttar dete hi aap pehla padaw paar karjayenge or 10,000 or rupay lekar hi jayenge\n")
        e1.insert(END, "  "+name+" ji aapka PANCHWA PRASHNA pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")
    if number==4:
        m = "3,000" 
        curr = "5,000"
        currlbd = curr.replace(",","")
        mon4.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q4.configure(bg="yellow", fg="black")
        mon3.configure(bg="#5B0A91", fg="white")
        q3.configure(bg="#5B0A91", fg="white")

        e1.delete(1.0, END)
        e1.insert(1.0, "\n")
        e1.insert(END, "  "+name+" ji aapka CHOTHA prashna pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")
    if number==3:
        m = "2,000" 
        curr = "3,000"
        currlbd = curr.replace(",","")
        mon3.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q3.configure(bg="yellow", fg="black")
        mon2.configure(bg="#5B0A91", fg="white")
        q2.configure(bg="#5B0A91", fg="white")
        
        e1.delete(1.0, END)
        e1.insert(1.0, "\n")
        e1.insert(END, "  "+name+" ji aapka TEESRA prashna pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")
    if number==2:
        m = "1,000" 
        curr = "2,000"
        currlbd = curr.replace(",","")
        mon2.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q2.configure(bg="yellow", fg="black")
        mon1.configure(bg="#5B0A91", fg="white")
        q1.configure(bg="#5B0A91", fg="white")

        e1.delete(1.0, END)
        e1.insert(1.0, "\n")
        e1.insert(END, "  "+name+" ji aapka TEESRA prashna pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")
    if number==1:
        m = "0" 
        curr = "1,000"
        currlbd = curr.replace(",","")
        mon1.configure(bg="yellow", fg="black")          #HIGHLIGHT THE QUESTION NUMBER ON LIST PANEL
        q1.configure(bg="yellow", fg="black")
        
        e1.delete(1.0, END)
        e1.insert(1.0, " \n")
        e1.insert(2.0, "Dewiyo or sajjano aaj hamare saath hotseat par bethe hai "+state+" se aye "+age+" warshiye "+name+" ji.\n")
        e1.insert(END, "To bina koi wakh barbad karte hue badte hai aapki pehle prashna ki taraf.\n")
        e1.insert(END, "To "+name+" ji aapka PEHLA prashna pure ₹"+curr+" ke liye aapki computer screen par yeh raha . . . . . *dhunununu*\n")


    if number==1 or number==16:
        while kpl<15:
        	e1.after(de*2, lambda: winsound.PlaySound('introkbc.wav', winsound.SND_ALIAS | winsound.SND_ASYNC))   #ONLY FOR QUESTION 1 and 16

        	e1.after(de*i, lambda: e1.configure(bg="white", fg="black"))
        	e1.after(de*(i+1), lambda: e1.configure(bg="#5B0A91", fg="white"))
        	e1.after(de*(i+2), lambda: e1.configure(bg="white", fg="black"))
        	e1.after(de*(i+3), lambda: e1.configure(bg="#5B0A91", fg="white"))

        	e2.after(de*i, lambda: e2.configure(bg="white", fg="black"))
        	e2.after(de*(i+1), lambda: e2.configure(bg="#5B0A91", fg="white"))
        	e2.after(de*(i+2), lambda: e2.configure(bg="white", fg="black"))
        	e2.after(de*(i+3), lambda: e2.configure(bg="#5B0A91", fg="white"))

        	e3.after(de*i, lambda: e3.configure(bg="white", fg="black"))
        	e3.after(de*(i+1), lambda: e3.configure(bg="#5B0A91", fg="white"))
        	e3.after(de*(i+2), lambda: e3.configure(bg="white", fg="black"))
        	e3.after(de*(i+3), lambda: e3.configure(bg="#5B0A91", fg="white"))
        	
        	BA.after(de*i, lambda: BA.configure(bg="white", fg="black"))
        	BA.after(de*(i+1), lambda: BA.configure(bg="#5B0A91", fg="white"))
        	BA.after(de*(i+2), lambda: BA.configure(bg="white", fg="black"))
        	BA.after(de*(i+3), lambda: BA.configure(bg="#5B0A91", fg="white"))
        	
        	OA.after(de*i, lambda: OA.configure(bg="white", fg="black"))
        	OA.after(de*(i+1), lambda: OA.configure(bg="#C5B358"))
        	OA.after(de*(i+2), lambda: OA.configure(bg="white", fg="black"))
        	OA.after(de*(i+3), lambda: OA.configure(bg="#C5B358"))

        	BB.after(de*i, lambda: BB.configure(bg="white", fg="black"))
        	BB.after(de*(i+1), lambda: BB.configure(bg="#5B0A91", fg="white"))
        	BB.after(de*(i+2), lambda: BB.configure(bg="white", fg="black"))
        	BB.after(de*(i+3), lambda: BB.configure(bg="#5B0A91", fg="white"))
        	
        	OB.after(de*i, lambda: OB.configure(bg="white", fg="black"))
        	OB.after(de*(i+1), lambda: OB.configure(bg="#C5B358"))
        	OB.after(de*(i+2), lambda: OB.configure(bg="white", fg="black"))
        	OB.after(de*(i+3), lambda: OB.configure(bg="#C5B358"))
        	
        	BC.after(de*i, lambda: BC.configure(bg="white", fg="black"))
        	BC.after(de*(i+1), lambda: BC.configure(bg="#5B0A91", fg="white"))
        	BC.after(de*(i+2), lambda: BC.configure(bg="white", fg="black"))
        	BC.after(de*(i+3), lambda: BC.configure(bg="#5B0A91", fg="white"))
        	
        	OC.after(de*i, lambda: OC.configure(bg="white", fg="black"))
        	OC.after(de*(i+1), lambda: OC.configure(bg="#C5B358"))
        	OC.after(de*(i+2), lambda: OC.configure(bg="white", fg="black"))
        	OC.after(de*(i+3), lambda: OC.configure(bg="#C5B358"))
        	
        	BD.after(de*i, lambda: BD.configure(bg="white", fg="black"))
        	BD.after(de*(i+1), lambda: BD.configure(bg="#5B0A91", fg="white"))
        	BD.after(de*(i+2), lambda: BD.configure(bg="white", fg="black"))
        	BD.after(de*(i+3), lambda: BD.configure(bg="#5B0A91", fg="white"))
        	
        	OD.after(de*i, lambda: OD.configure(bg="white", fg="black"))
        	OD.after(de*(i+1), lambda: OD.configure(bg="#C5B358"))
        	OD.after(de*(i+2), lambda: OD.configure(bg="white", fg="black"))
        	OD.after(de*(i+3), lambda: OD.configure(bg="#C5B358"))

        	dispopt.after(de*i, lambda: dispopt.configure(bg="white", fg="black"))
        	dispopt.after(de*(i+1), lambda: dispopt.configure(bg="#C5B358"))
        	dispopt.after(de*(i+2), lambda: dispopt.configure(bg="white", fg="black"))
        	dispopt.after(de*(i+3), lambda: dispopt.configure(bg="#C5B358"))
        	
        	lockb.after(de*i, lambda: lockb.configure(bg="white", fg="black"))
        	lockb.after(de*(i+1), lambda: lockb.configure(bg="#5B0A91", fg="white"))
        	lockb.after(de*(i+2), lambda: lockb.configure(bg="white", fg="black"))
        	lockb.after(de*(i+3), lambda: lockb.configure(bg="#5B0A91", fg="white"))
        	
        	confb.after(de*i, lambda: confb.configure(bg="white", fg="black"))
        	confb.after(de*(i+1), lambda: confb.configure(bg="#5B0A91", fg="white"))
        	confb.after(de*(i+2), lambda: confb.configure(bg="white", fg="black"))
        	confb.after(de*(i+3), lambda: confb.configure(bg="#5B0A91", fg="white"))

        	eyour.after(de*i, lambda: eyour.configure(bg="white", fg="black"))
        	eyour.after(de*(i+1), lambda: eyour.configure(bg="#5B0A91", fg="white"))
        	eyour.after(de*(i+2), lambda: eyour.configure(bg="white", fg="black"))
        	eyour.after(de*(i+3), lambda: eyour.configure(bg="#5B0A91", fg="white"))
        	
        	ecorr.after(de*i, lambda: ecorr.configure(bg="white", fg="black"))
        	ecorr.after(de*(i+1), lambda: ecorr.configure(bg="#5B0A91", fg="white"))
        	ecorr.after(de*(i+2), lambda: ecorr.configure(bg="white", fg="black"))
        	ecorr.after(de*(i+3), lambda: ecorr.configure(bg="#5B0A91", fg="white"))
        	
        	tact.after(de*i, lambda: tact.configure(bg="white", fg="black"))
        	tact.after(de*(i+1), lambda: tact.configure(bg="#5B0A91", fg="white"))
        	tact.after(de*(i+2), lambda: tact.configure(bg="white", fg="black"))
        	tact.after(de*(i+3), lambda: tact.configure(bg="#5B0A91", fg="white"))
        	
        	rup.after(de*i, lambda: rup.configure(bg="white", fg="black"))
        	rup.after(de*(i+1), lambda: rup.configure(bg="#5B0A91", fg="white"))
        	rup.after(de*(i+2), lambda: rup.configure(bg="white", fg="black"))
        	rup.after(de*(i+3), lambda: rup.configure(bg="#5B0A91", fg="white"))
        	
        	moneye.after(de*i, lambda: moneye.configure(bg="black", fg="white"))
        	moneye.after(de*(i+1), lambda: moneye.configure(bg="white", fg="black"))
        	moneye.after(de*(i+2), lambda: moneye.configure(bg="black", fg="white"))
        	moneye.after(de*(i+3), lambda: moneye.configure(bg="white", fg="black"))
            
        	rbut.after(de*i, lambda: rbut.configure(bg="white", fg="black"))
        	rbut.after(de*(i+1), lambda: rbut.configure(bg="#5B0A91", fg="white"))
        	rbut.after(de*(i+2), lambda: rbut.configure(bg="white", fg="black"))
        	rbut.after(de*(i+3), lambda: rbut.configure(bg="#5B0A91", fg="white"))
        	   	
        	if number ==1:
        	    pass
        	else:

        	    e2.delete(0, END)
        	    e3.delete(0, END)
        	    OA.delete(0, END)
        	    OB.delete(0, END)
        	    OC.delete(0, END)
        	    OD.delete(0, END)

        	
        	nbut.after(de*i, lambda: nbut.configure(bg="white", fg="black"))
        	nbut.after(de*(i+1), lambda: nbut.configure(bg="#5B0A91", fg="white"))
        	nbut.after(de*(i+2), lambda: nbut.configure(bg="white", fg="black"))
        	nbut.after(de*(i+3), lambda: nbut.configure(bg="#5B0A91", fg="white"))

        	qbut.after(de*i, lambda: qbut.configure(bg="white", fg="black"))
        	qbut.after(de*(i+1), lambda: qbut.configure(bg="#5B0A91", fg="white"))
        	qbut.after(de*(i+2), lambda: qbut.configure(bg="white", fg="black"))
        	qbut.after(de*(i+3), lambda: qbut.configure(bg="#5B0A91", fg="white"))

        	kpl += 1
        	i += 4

        e2.after(9020, lambda: e2.insert(0, "           "+"Q"+str(number)))
        e3.after(9001, lambda: e3.insert(0, "      "+QUESTION))
        OPTAs = OPTA.capitalize()
        OPTBs = OPTB.capitalize()
        OPTCs = OPTC.capitalize()                                          #PRINT STUFF ON SCREEN AFTER BLINKING WIDGETS
        OPTDs = OPTD.capitalize()
        OA.after(9001, lambda: OA.insert(0, "  "+OPTAs))
        OB.after(9001, lambda: OB.insert(0, "  "+OPTBs))
        OC.after(9001, lambda: OC.insert(0, "  "+OPTCs))
        OD.after(9001, lambda: OD.insert(0, "  "+OPTDs))                                              
    
    if number>1 and number<16:

        e1.after(de*9, lambda: winsound.PlaySound('KBC NXTQ.wav', winsound.SND_ALIAS | winsound.SND_ASYNC))            #FROM QUESTION 2 TO 15

        e2.delete(0, END)
        e2.after(de*14, lambda: e2.configure(bg="white", fg="black"))
        e2.after(de*15, lambda: e2.configure(bg="#5B0A91", fg="white"))
        e2.after(de*16, lambda: e2.configure(bg="white", fg="black"))
        e2.after(de*17, lambda: e2.configure(bg="#5B0A91", fg="white"))
        e2.after(de*18, lambda: e2.configure(bg="white", fg="black"))
        e2.after(de*19, lambda: e2.configure(bg="#5B0A91", fg="white"))
        e2.after(de*20, lambda: e2.insert(0, "           "+"Q"+str(number)))

        e3.delete(0, END)
        e3.after(de*14, lambda: e3.configure(bg="white", fg="black"))
        e3.after(de*15, lambda: e3.configure(bg="#5B0A91", fg="white"))
        e3.after(de*16, lambda: e3.configure(bg="white", fg="black"))
        e3.after(de*17, lambda: e3.configure(bg="#5B0A91", fg="white"))
        e3.after(de*18, lambda: e3.configure(bg="white", fg="black"))
        e3.after(de*19, lambda: e3.configure(bg="#5B0A91", fg="white"))
        e3.after(de*20, lambda: e3.insert(0, "      "+QUESTION))

        OPTAs = OPTA.capitalize()
        OPTBs = OPTB.capitalize()
        OPTCs = OPTC.capitalize()
        OPTDs = OPTD.capitalize()
        OA.delete(0, END)
        OA.after(de*14, lambda: OA.configure(bg="white", fg="black"))
        OA.after(de*15, lambda: OA.configure(bg="#5B0A91", fg="white"))
        OA.after(de*16, lambda: OA.configure(bg="white", fg="black"))
        OA.after(de*17, lambda: OA.configure(bg="#5B0A91", fg="white"))
        OA.after(de*18, lambda: OA.configure(bg="white", fg="black"))
        OA.after(de*19, lambda: OA.configure(bg="#C5B358"))
        OA.after(de*20, lambda: OA.insert(0, "  "+OPTAs))
 
        OB.delete(0, END)
        OB.after(de*14, lambda: OB.configure(bg="white", fg="black"))
        OB.after(de*15, lambda: OB.configure(bg="#5B0A91", fg="white"))
        OB.after(de*16, lambda: OB.configure(bg="white", fg="black"))
        OB.after(de*17, lambda: OB.configure(bg="#5B0A91", fg="white"))
        OB.after(de*18, lambda: OB.configure(bg="white", fg="black"))
        OB.after(de*19, lambda: OB.configure(bg="#C5B358"))
        OB.after(de*20, lambda: OB.insert(0, "  "+OPTBs))
        
        OC.delete(0, END)
        OC.after(de*14, lambda: OC.configure(bg="white", fg="black"))
        OC.after(de*15, lambda: OC.configure(bg="#5B0A91", fg="white"))
        OC.after(de*16, lambda: OC.configure(bg="white", fg="black"))
        OC.after(de*17, lambda: OC.configure(bg="#5B0A91", fg="white"))
        OC.after(de*18, lambda: OC.configure(bg="white", fg="black"))
        OC.after(de*19, lambda: OC.configure(bg="#C5B358"))
        OC.after(de*20, lambda: OC.insert(0, "  "+OPTCs))
        
        OD.delete(0, END)
        OD.after(de*14, lambda: OD.configure(bg="white", fg="black"))
        OD.after(de*15, lambda: OD.configure(bg="#5B0A91", fg="white"))
        OD.after(de*16, lambda: OD.configure(bg="white", fg="black"))
        OD.after(de*17, lambda: OD.configure(bg="#5B0A91", fg="white"))
        OD.after(de*18, lambda: OD.configure(bg="white", fg="black"))
        OD.after(de*19, lambda: OD.configure(bg="#C5B358"))
        OD.after(de*20, lambda: OD.insert(0, "  "+OPTDs))



    #THIS SEGMENT WILL BE FOR THE QUESTIONS OTHER THAN Q1
    print("DONE")
    dispopt.delete(0, END)
    eyour.delete(0, END)
    eyour.insert(0, "YOUR ANSWER IS . . . . .")
    tact.delete(1.0, END)
    moneye.delete(0, END)
    moneye.insert(0, m)


    



#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#
#      L               EEEEEEEEEE      AAAAAAAAAAAA    kDDDDD        
#      L               E               A          A    D       D  
#      L               E               A          A    D        D 
#      L               E               A          A    D         D
#      L               E               A          A    D         D
#      L               E               AAAAAAAAAAAA    D         D
#      L               EEEEEEEE        A          A    D         D
#      L               E               A          A    D         D
#      L               E               A          A    D         D
#      L               E               A          A    D         D
#      L               E               A          A    D        D
#      L               E               A          A    D       D  
#      LLLLLLLLLLL     EEEEEEEEEEE     A          A    DDDDDDDD   
#
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

def LEADERBOARD():
    winsound.PlaySound('btn.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    print(won)
    print(wonlbd)
    mycursor.execute('insert into user(Name,Age,State,Won,WonLBD) values (?,?,?,?,?)',(name, age, state, won, wonlbd))
    con.commit()

    
    #BACKGROND IMAGE
    global img
    path=".\img\KK3O.jpg"
    k = Image.open(path)
    k = k.resize((1400, 800), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(k)
    ldrbrd = Label(root, bg="#C5B358", image=img)
    ldrbrd.place(relwidth=1, relheight=1)

    ldbdFR = Frame(ldrbrd, bg="#C5B358", bd=10, relief="ridge")
    ldbdFR.place(relheight=0.18, relwidth=0.8, relx=0.1, rely=0.07)
    ldbd = Label(ldbdFR, bg="#5B0A91", fg="white", font=myfontH, text="LEADERBOARD")
    ldbd.place(relwidth=1, relheight=1)


    #TABLE
    TABLfr = Frame(ldrbrd, bg="#C5B358", bd=10, relief="ridge")
    TABLfr.place(relx=0.1, rely=0.28, relwidth=0.8, relheight=0.65)

    Trank = Label(TABLfr, bg="black", fg="white", text="RANK", relief="raised", bd=4).place(relheight=0.1, relwidth=0.1, relx=0.001)
    Tname = Label(TABLfr, bg="black", fg="white", text="NAME", relief="raised", bd=4).place(relheight=0.1, relwidth=0.4, relx=0.102)
    Tage = Label(TABLfr, bg="black", fg="white", text="AGE", relief="raised", bd=4).place(relheight=0.1, relwidth=0.15, relx=0.503)
    Tstate = Label(TABLfr, bg="black", fg="white", text="STATE", relief="raised", bd=4).place(relheight=0.1, relwidth=0.15, relx=0.654)
    Twon = Label(TABLfr, bg="black", fg="white", text="WON", relief="raised", bd=4).place(relheight=0.1, relwidth=0.194, relx=0.805)


    frame=Frame(TABLfr,width=300,height=300)
    frame.place(relwidth=1, relheight=0.9, rely=0.1)

    canvass=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,800,800))
    vbar=Scrollbar(frame,orient=VERTICAL)
    vbar.pack(side=RIGHT,fill=Y)
    vbar.config(command=canvass.yview)
    canvass.config(width=300,height=300)
    canvass.config(yscrollcommand=vbar.set)
    canvass.pack(side=LEFT,expand=True,fill=BOTH)

#user
    f = Frame(canvass, bg="#5B0A91")
    f.place(relwidth=1, relheight=1)

    EXITfr = Frame(ldrbrd , bg="#C5B358", bd=10, relief="ridge")
    EXITfr.place(relx=0.93,rely=0.8, relwidth=0.05, relheight=0.09)
    EXIT = Button(EXITfr, bg="#5B0A91", fg="#ffffff", font=myfont, text="EXT", command=exite)                               #EXIIIIIIT COMMMMAAAAAAAAAAAAAAAAAAND #########################
    EXIT.place(relwidth=1, relheight=1)


    mycursor.execute("select count(*) from user")                      #COUNTING NUMBER OF ROWS
    for k in mycursor:
        ROWS = k[0]
    

    currentr = 0                            
    d = {}                                                            #DICTIONARY DEFINED
    totalROWS = 20                                                    #TOTAL ROWS TO BE PUT ON SCREEN




    for i in range(1,totalROWS+1):
        d["Nt{}".format(i)] = ""
        d["At{}".format(i)] = ""                                   #DICTIONARY SETTING KEY AND ASSIGNING "" AS VALUE
        d["St{}".format(i)] = ""
        d["Wt{}".format(i)] = ""

    while currentr!=ROWS:                                                                          #LOOP TO ITERATE ROW NO. OF TIMES
        mycursor.execute("select * from user order by WonLBD desc LIMIT {},1".format(currentr))    #IMPORTING A ROW FROM TABLE
        for i in mycursor:
            d["Nt{}".format(currentr+1)] = i[0]
            d["At{}".format(currentr+1)] = i[1]                    #DICTIONARY THAT STORES NAME,AGE,STATE,WON OF EACH PLAYER
            d["St{}".format(currentr+1)] = i[2]
            d["Wt{}".format(currentr+1)] = i[3]
        currentr +=1



    toppadding = 1
    R=1
    while R!=totalROWS:
        rankt1 = Label(canvass, text = R)
        rankt1.configure(width = 14, height=2, relief = "sunken")
        rankt1_window = canvass.create_window(1, toppadding, anchor=NW, window=rankt1)        #WINDOW   - TO PLACE A WIDGIT ON TOP OF A CANVAS
        namet1 = Label(canvass, text = d["Nt{}".format(R)])
        namet1.configure(width = 60, height=2, relief = "sunken")
        namet1_window = canvass.create_window(109, toppadding, anchor=NW, window=namet1)
        aget1 = Label(canvass, text = d["At{}".format(R)])
        aget1.configure(width = 22, height=2, relief = "sunken")
        aget1_window = canvass.create_window(540, toppadding, anchor=NW, window=aget1)
        statet1 = Label(canvass, text = d["St{}".format(R)])
        statet1.configure(width = 22, height=2, relief = "sunken")
        statet1_window = canvass.create_window(702, toppadding, anchor=NW, window=statet1)
        wont1 = Label(canvass, text = d["Wt{}".format(R)])
        wont1.configure(width = 26, height=2, relief = "sunken")
        wont1_window = canvass.create_window(865, toppadding, anchor=NW, window=wont1)
        R += 1
        toppadding += 41
















#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#
#   qqqqqqqqq     U      U    IIIII   TTTTTTT
#   q       q     U      U      I        T
#   q       q     U      U      I        T
#   q     q q     U      U      I        T
#   q      qq     U      U      I        T
#   qqqqqqqqq      UUUUUU     IIIII      T
#            q    
#             q   
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

def QUIT():
    winsound.PlaySound('btn.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    
    global won
    global wonlbd

    if number==1:
        won = 0
        wonlbd = 0


    global quitBG
    quitBG = Label(root, bg="#C5B358")
    quitBG.place(relwidth=1, relheight=1)
    quitFR = Frame(quitBG, bg="#C5B358", bd=10, relief="ridge")
    quitFR.place(relwidth=0.7, relheight=0.35, relx=0.5, rely=0.23, anchor='n')                      #QUIT BUTTON POPUP MENU
    myfont = f.Font(family='Maiandra GD')
    quitPOP = Label(quitFR, bg="#5B0A91", fg="white", font=myfont, text="Are you sure you want to quit the game on Q"+str(number))
    quitPOP.place(relwidth=1, relheight=1)
    
    #MONEY COUNTER
    global moneyf
    moneyf = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    moneyf.place(relx=0.4, rely=0.6, relwidth=0.19, relheight=0.08)
    myfont = f.Font(family='Maiandra GD')
    rup = Label(moneyf, bg="#5B0A91", fg="white", font=myfont, relief="raised", text="₹")            #MONEY COUNTER
    rup.place(relx=0.015, rely=0.04, relwidth=0.3, relheight=0.85)
    moneye = Entry(moneyf, bg="white", font=myfont,relief="sunken")
    moneye.place(relx=0.35, rely=0.04, relwidth=0.635, relheight=0.85)

    #YES
    global yesFR
    yesFR = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    yesFR.place(relx=0.2, rely=0.6, relwidth=0.15, relheight=0.08)
    yes = Button(yesFR, bg="#5B0A91", fg="white", font=myfont, text="YES", command=LEADERBOARD)      #WHEN PRESSED YES
    yes.place(relwidth=1, relheight=1)

    #NO
    global noFR
    noFR = Frame(root, bg="#C5B358", bd=10, relief="ridge")
    noFR.place(relx=0.65, rely=0.6, relwidth=0.15, relheight=0.08)
    no = Button(noFR, bg="#5B0A91", fg="white", font=myfont, text="NO", command=qno)                 #WHEN PRESSSED NO
    no.place(relwidth=1, relheight=1)

    moneye.delete(0, END)
    moneye.insert(0, won)
    print(won)

def qno():
    winsound.PlaySound('btn.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    quitBG.place_forget()
    moneyf.place_forget()
    yesFR.place_forget()
    noFR.place_forget()









#Oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#  RRRRRRRRRRRR    EEEEEEEEEEEEEEEEE    V                       V
#  R          R    E                     V                     V
#  R          R    E                      V                   V
#  R          R    E                       V                 V
#  R          R    E                        V               V
#  R          R    E                         V             V
#  RRRRRRRRRRRR    EEEEEEEEEEEE               V           V          
#  R               E                           V         V
#  R R             E                            V       V
#  R   R           E                             V     V
#  R     R         E                              V   V
#  R       R       E                               V V
#  R         R     EEEEEEEEEEEEEEEEE                V
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

rev = 3
def REVIVE():
    winsound.PlaySound('btn.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    
    #won
    global rbut
    rbut.configure(state=DISABLED)
    confb.configure(state=DISABLED)

    myfont = f.Font(family='Maiandra GD')


    global agla
    if number==16:
        agla = "NAHI"
    if number==15:
        agla = "Sollvey" 
    if number==14:
        agla = "Pandrhawe"
    if number==13:
        agla = "Chodwe"
    if number==12:
        agla = "Terwe"
    if number==11:
        agla = "Barwe"
    if number==10:
        agla = "Gyarwe"
    if number==9:
        agla = "Daswe"
    if number==8:
        agla = "Nawe"
    if number==7:
        agla = "Aathwe"
    if number==6:
        agla = "Satwe"
    if number==5:
        agla = "Chhate"
    if number==4:
        agla = "Panchwe"
    if number==3:
        agla = "Chothe"
    if number==2:
        agla = "Teesre"
    if number==1:
        agla = "Dusre"


    global rev
    rev-=1

    global Fimg
    global Eimg
    global l1
    global l2
    global l3
    pathF = ".\img\ill.png"
    pathE = ".\img\emp.png"

    kF = Image.open(pathF)
    kF = kF.resize((50, 50), Image.ANTIALIAS)
    Fimg = ImageTk.PhotoImage(kF)

    kE = Image.open(pathE)
    kE = kE.resize((50, 50), Image.ANTIALIAS)
    Eimg = ImageTk.PhotoImage(kE)

    tact.configure(font=myfont)
    if rev == 2:
        l1 = Label(revboxppl, image=Eimg, bg="#5B0A91")
        l1.place(relheight=1, relwidth=0.3)
        l2 = Label(revboxppl, image=Fimg, bg="#5B0A91")
        l2.place(relheight=1, relwidth=0.3, relx=0.345)
        l3 = Label(revboxppl, image=Fimg, bg="#5B0A91")
        l3.place(relheight=1, relwidth=0.3, relx=0.696)
        print("2 lifelines left")
    if rev==1:
        l1 = Label(revboxppl, image=Eimg, bg="#5B0A91")
        l1.place(relheight=1, relwidth=0.3)
        l2 = Label(revboxppl, image=Eimg, bg="#5B0A91")
        l2.place(relheight=1, relwidth=0.3, relx=0.345)
        l3 = Label(revboxppl, image=Fimg, bg="#5B0A91")
        l3.place(relheight=1, relwidth=0.3, relx=0.696)
        print("1 lifelines left")
    if rev==0 or rev<0:
        l1 = Label(revboxppl, image=Eimg, bg="#5B0A91")
        l1.place(relheight=1, relwidth=0.3)
        l2 = Label(revboxppl, image=Eimg, bg="#5B0A91")
        l2.place(relheight=1, relwidth=0.3, relx=0.345)
        l3 = Label(revboxppl, image=Eimg, bg="#5B0A91")
        l3.place(relheight=1, relwidth=0.3, relx=0.696)
        print("0 lifelines left")
        revive = Frame(root, bg="green", bd=10, relief="ridge")
        revive.place(relwidth=0.06334, relheight=0.08, relx=0.73, rely=0.88)
        rbut = Button(revive, bg="#5B0A91", fg="white", font=myfont, text="REVIVE", state=DISABLED)
        rbut.place(relwidth=1, relheight=1)


    if ANSO == option:


        if option == "a":
            BA.configure(bg="green", fg="white")
            OA.configure(bg="green", fg="white")                                                  #green ON CHOSEN OPTION
        if option == "b":
            BB.configure(bg="green", fg="white")
            OB.configure(bg="green", fg="white")
        if option == "c":
            BC.configure(bg="green", fg="white")
            OC.configure(bg="green", fg="white")
        if option == "d":
            BD.configure(bg="green", fg="white")
            OD.configure(bg="green", fg="white")

        if number==16:

            #==========================#
            #|| SAME AS CONF CORRECT ||#
            #==========================#
            corr = Frame(root, bg="green", bd=15, relief="ridge")
            corr.place(relwidth=0.25, relheight=0.2, relx=0.06, rely=0.76)
            myfont = f.Font(family='Maiandra GD', size=46, weight="bold")
            ecorr = Entry(corr, bg="orange", fg="white", font=myfont)
            ecorr.place(relwidth=1, relheight=1)
            ecorr.delete(0, END)
            ecorr.insert(0, "CORECT")
            tact.delete(1.0, END)
            tact.insert(1.0, "\n")
            tact.insert(2.0, "Option ["+ANSO+"] "+ANSW+" was the correct answer ,\n")
            tact.insert(END, "CONGRATULATIONS you have won the game\n")
        else:
            corr = Frame(root, bg="green", bd=15, relief="ridge")
            corr.place(relwidth=0.25, relheight=0.2, relx=0.06, rely=0.76)
            myfont = f.Font(family='Maiandra GD', size=46, weight="bold")
            ecorr = Entry(corr, bg="orange", fg="white", font=myfont)
            ecorr.place(relwidth=1, relheight=1)
            ecorr.delete(0, END)
            ecorr.insert(0, "CORECT")
            tact.delete(1.0, END)
            tact.insert(1.0, "\n")
            tact.insert(2.0, "Option ["+ANSO+"] "+ANSW+" was the correct answer ,\nYou wasted one of your lifeline ....\n")
            tact.insert(END, "lmao, Only "+str(rev)+" lifelines left\n")
            tact.insert(END, "badte hai "+agla+" prashna ki oor\n")
    else:

        if option == "a":
            BA.configure(bg="red", fg="white")
            OA.configure(bg="red", fg="white")                                                  #red ON WRONG OPTION
        if option == "b":
            BB.configure(bg="red", fg="white")
            OB.configure(bg="red", fg="white")
        if option == "c":
            BC.configure(bg="red", fg="white")
            OC.configure(bg="red", fg="white")
        if option == "d":
            BD.configure(bg="red", fg="white")
            OD.configure(bg="red", fg="white")


        if ANSO == "a":
            BA.configure(bg="green", fg="white")
            OA.configure(bg="green", fg="white")                                                  #green ON THE ACTUAL CORRECT AMSWER 
        if ANSO == "b":
            BB.configure(bg="green", fg="white")
            OB.configure(bg="green", fg="white")
        if ANSO == "c":
            BC.configure(bg="green", fg="white")
            OC.configure(bg="green", fg="white")
        if ANSO == "d":
            BD.configure(bg="green", fg="white")
            OD.configure(bg="green", fg="white")

        if number==16:
            #==========================#
            #|| SAME AS CONF CORRECT ||#
            #==========================#
            corr = Frame(root, bg="red", bd=15, relief="ridge")
            corr.place(relwidth=0.25, relheight=0.2, relx=0.06, rely=0.76)
            myfont = f.Font(family='Maiandra GD', size=46, weight="bold")
            ecorr = Entry(corr, bg="orange", fg="white", font=myfont)
            ecorr.place(relwidth=1, relheight=1)
            ecorr.delete(0, END)
            ecorr.insert(0, "WRONG")
            tact.delete(1.0, END)
            tact.insert(1.0, "\nAgar aap Option ["+option+"] "+optionW+" ke saath gaye hote to aapka uttar \ngalat hota Is prashn ka sahi jawaab hai Option ["+ANSO+"] "+ANSW+"\n")
            tact.insert(END, "Ek bohot acha faisla, CONGRATULATIONS you have won the game\n")

            
        else:
            corr = Frame(root, bg="red", bd=15, relief="ridge")
            corr.place(relwidth=0.25, relheight=0.2, relx=0.06, rely=0.76)
            myfont = f.Font(family='Maiandra GD', size=46, weight="bold")
            ecorr = Entry(corr, bg="orange", fg="white", font=myfont)
            ecorr.place(relwidth=1, relheight=1)
            ecorr.delete(0, END)
            ecorr.insert(0, "WRONG")
            tact.delete(1.0, END)
            tact.insert(1.0, "\nAgar aap Option ["+option+"] "+optionW+" ke saath gaye hote to aapka uttar \ngalat hota Is prashn ka sahi jawaab hai Option ["+ANSO+"] "+ANSW+"\n")
            tact.insert(END, "Ek bohot acha faisla, Only "+str(rev)+" lifelines left\n")
            tact.insert(END, "badte hai "+agla+" prashna ki oor\n")
    
    global won
    global wonlbd
    won = curr
    wonlbd = currlbd
    if number!=16:
        moneye.delete(0, END)
        moneye.insert(0, won)
        nbut.configure(state=NORMAL, command=functioning)
    else:
        nbut.configure(text="END", state=NORMAL, command=LEADERBOARD)


#QUIT
def exite():
    root.destroy()







#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

#   BBBBBBBB     OOOOOOOOOO     DDDDDDD       Y       Y
#   B       B    O        O     D      D       Y     Y
#   B       B    O        O     D       D       Y   Y
#   B       B    O        O     D       D        Y Y
#   B       B    O        O     D       D         Y
#   BBBBBBBB     O        O     D       D         Y
#   B       B    O        O     D       D         Y
#   B       B    O        O     D       D         Y
#   B       B    O        O     D       D         Y
#   B       B    O        O     D      D          Y
#   BBBBBBBB     OOOOOOOOOO     DDDDDDD           Y

#oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

path=".\img\KK3O.jpg"                           #PURPLE BACKGROUND IMAGEPATH
k = Image.open(path)
k = k.resize((1400, 800), Image.ANTIALIAS)      #RESIZING THE IMAGE TO FIT IN
img = ImageTk.PhotoImage(k)
label = Label(root, image=img)
label.place(relwidth=1, relheight=1)

path1 = ".\img\K.png"                           #KBC LOGO IN THE HOMEPAGE
k1 = Image.open(path1)
k1 = k1.resize((300,335), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(k1)
mainfrm = Frame(root, bg="#C5B358", relief="raised", bd=10)            #KBC LOGO FRAME
mainfrm.place(width=300, height=335,relx=0.5, rely=0.1, anchor='n')
head = Label(mainfrm, image=logo)                                      #KBC LOGO CONTAINER
head.place(relwidth=1, relheight=1)


namel = Label(root, text="Name   :", font=myfont, bg="#C5B358",  bd=4, relief="raised")          #NAME
namel.place(relx=0.4, rely=0.57, relwidth=0.08, anchor='n')
nameE = Entry(root, font=myfont, bd=2, relief="sunken")
nameE.place(relx=0.54, rely=0.57, width=265, anchor='n')

agel = Label(root, text="Age    :", font=myfont, bg="#C5B358",  bd=4, relief="raised")           #AGE
agel.place(relx=0.4, rely=0.62, relwidth=0.08, anchor='n')
ageE = Entry(root, font=myfont, bd=2, relief="sunken")
ageE.place(relx=0.54, rely=0.62, width=265, anchor='n')

statel = Label(root, text="State  :", font=myfont, bg="#C5B358", bd=4, relief="raised")          #state
statel.place(relx=0.4, rely=0.67, relwidth=0.08, anchor='n')
stateE = Entry(root, font=myfont, bd=2, relief="sunken")
stateE.place(relx=0.54, rely=0.67, width=265, anchor='n')


button = Button(root, text="START", font=myfont, borderwidth=10, bg="#C5B358", command=start)    #"START" BUTTON
button.place(relx=0.5, rely=0.735, relwidth=0.235, anchor='n')



#PROGRAM LOOP ENDING---------------------------------------------
root.mainloop()


