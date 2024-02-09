from tkinter import * # import library to use tkinter
import random
from varname import nameof  #  pip3 install varname
import os
import sys
import pygame 

from define import *

#-------------------------------------------------------------------------------------------------#

#Call class of pygame to built music function
pygame.mixer.init()

#Setup up frame for app game
window = Tk()
window.geometry("400x600+900+50") #set weight height and location for app when it appear on screen
window.iconbitmap(".\img\HoanHK.ico") #Set icon
window.title("MasterMind - Cre: Ha Khai Hoan K17") # Set game name
window["bg"] = WINDOW_COLOR     #set color for bg app
#set size limit 
window.maxsize(width=400, height=600)  
window.minsize(width=400, height=600)

#Built a function to play music
def play_music():
    pygame.mixer.music.load(".\music\music.mp3")
    pygame.mixer.music.play(loops=0)

#Built a function to play music    
def stop_music():
    pygame.mixer.music.stop()
    
count_round = [] #a list which is used to count round (this game has 10 round)
color_list = ["#006600","#FFFF33","#0033CC","#FF0000","#660099","#CC66FF","#FF6600","#66FFFF"] # color to random
score_list = [] # list score

# create variable score for list, they will be used evaluate rank player
for i in range(90,-1,-10): 
    score_list.append(i)
# built number row list
list_row_label = []
list_row_label_result = []
for i in range(1,11):
    for j in range(1,5):
        list_row_label.append(str(i))
        list_row_label_result.append(str(i))
#built list to set label for 10 round
list_label = []
for i in range(1,11):
    for j in range(1,5):
        list_label.append(str(j))
#built list to set result label for 10 round
row_result_list = []
for i in range(1,11):
    row_result_list.append(i)
#built a list which is used add color by player in 1 round (1 row)
EnterColor_list = []#
color_opposite = []# (color compare with)
color_opposite_no_number = []#(color opposite mask)
random_list = []# (a list to random number to set random color)
list_color_ToCheck = [] #list color to compare to value in EnterColor_list

# create value to add
for i in range(4):
        random_list.append(int(random.randint(0,7)))
       
for i in random_list:
    list_color_ToCheck.append(color_list[i])
# print("random:........",list_color_ToCheck)
# it will be called when player win game
def You_win_label():
    Label(window,text = "You win" + ", score: "+ str(score_list[0] + 10),font = ("Terminal",10), width=30, height=2,fg = RED_COLOR,borderwidth=2,relief="solid").place(x =120 , y =555)
    Label(window, text = "Result:",bg = WINDOW_COLOR, fg = BLUE_COLOR, font = ("Terminal",14)).place(x =44, y = 557)
# it will be called when player lose game
def You_lose_label():
    Label(window,text = "You lose",font = ("Terminal",10), width=30, height=2,fg = RED_COLOR,borderwidth=2,relief="solid").place(x =120 , y =555)
    Label(window, text = "Result:",bg = WINDOW_COLOR, fg = BLUE_COLOR, font = ("Terminal",14)).place(x =44, y = 557)
# it will be called when player Press the play again button
def restart_program():
    sys.stdout.flush()
    os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
# it will be called when player Press the exit button
def exit_program():
    window.destroy()
# bulte a function, which will set up Label Result Color variable name
def ChangeLabelResultColor(bg_color,count_label,number_row):
    name = "LabelResult" + count_label + "_r"+ number_row
    name_new = globals()[name]
    name_new['bg'] = bg_color
# Setup button when player click, color will light
def SetButtonClickOnColor(bg_color,x,y):
    Button(window, bg = bg_color ,width= 6,height= 2,command=lambda:ChangeLabelColor(bg_color)).place(x = x, y = y)
# it will build a label mask in front of color button
def SetMaskLabelColor(bg_color,x,y):
    Label(window, bg = bg_color ,width= 6,height= 2).place(x = x, y = y)
# it will build label which has show correct answer function
def SetColorResult_end_system(color_end,x,y):
    Label(window, bg = color_end, width= 5,height=2,borderwidth=2,relief="solid").place(x  = x , y = y)
# setup a function, it will have program show a notification
def TheEndNoti():
    #Show Correct answers
    Label(window,text = "",font = ("Terminal",30),pady=150,width=2 ,bg = WINDOW_COLOR).place(x  = 330, y = 190)
    SetMaskLabelColor(JADE_COLOR,340,200)
    SetMaskLabelColor(GREEN_COLOR,340,240)
    SetMaskLabelColor(YELLOW_COLOR,340,280)
    SetMaskLabelColor(BLUE_COLOR,340,320)
    SetMaskLabelColor(RED_COLOR,340,360)
    SetMaskLabelColor(PINK_COLOR,340,400)
    SetMaskLabelColor(ORANGE_COLOR,340,440)
    SetMaskLabelColor(PURPLE_COLOR,340,480)
    # Build The End notification
    Label(window,text = "The End",font = ("Terminal",30),padx=20,pady=50,width=10 ,borderwidth=3,relief="solid",bg = LIGHT_WHITE_RESULT_COLOR).place(x  = 30, y = 220)
    SetColorResult_end_system(list_color_ToCheck[0],90,320)
    SetColorResult_end_system(list_color_ToCheck[1],156,320)
    SetColorResult_end_system(list_color_ToCheck[2],220,320)
    SetColorResult_end_system(list_color_ToCheck[3],285,320)
    # setup play again button
    Button(window,text = "Play Again", font = ("Terminal",18),padx=8,pady=5,width=10 ,borderwidth=3,relief="solid",fg = RED_COLOR,bg = LIGHT_WHITE_RESULT_COLOR,
            command= lambda: restart_program()).place(x  = 110, y = 380)
    # setup Exit button
    Button(window,text = "Exit", font = ("Terminal",18),padx=8,pady=5,width=10 ,borderwidth=3,relief="solid",fg = RED_COLOR,bg = LIGHT_WHITE_RESULT_COLOR,
            command= lambda : exit_program() ).place(x  = 110, y = 445)
    # print("The end")
# This is the function that will show the player's score through each round
def Decrease_score(score):
    Label(window,text = score,font = ("Terminal",10), width=30, height=2,fg = RED_COLOR,borderwidth=2,relief="solid").place(x =120 , y =555)
# Turn light result after click on color button 4 time
def Turn_LightResult():
    
    #Create auxiliary lists, they wil have original list be not changed
    list_color_ToCheck_extra = []
    EnterColor_list_extra = []
    #add new value to above lists
    for i in list_color_ToCheck:
        list_color_ToCheck_extra.append(i)

    for i in EnterColor_list:
        EnterColor_list_extra.append(i)
    
    len_EnterColor = len(EnterColor_list_extra)
    for i in range(len_EnterColor):
        if EnterColor_list_extra[i] == list_color_ToCheck_extra[i]:
            color_opposite.append(i*10 + i)
            color_opposite_no_number.append(i) 
    
    # Algorithm Swap values to discard when traversed                       
    for i in color_opposite_no_number:
        EnterColor_list_extra[i] = "F"
        list_color_ToCheck_extra[i] = "F"
    
    mask_color = []
    mask_random = []
    
    for i in EnterColor_list_extra:
        if i != "F":
            mask_color.append(i)
    
    for i in list_color_ToCheck_extra:
        if i != "F":
            mask_random.append(i)
    
    len_mask_color = len(mask_color)
    
    for i in range(len_mask_color):
        for j in range(len_mask_color):
            if mask_random[i] == mask_color[j]:
                color_opposite.append("1")
                mask_random[i] = "RANDOM"
                mask_color[j] = "COLOR"
    
    while len(color_opposite) < 4:
        color_opposite.append("2")   
    #Turn result light        
    for i in range(len(color_opposite)):
        if int(color_opposite[i]) % 11 == 0:
            ChangeLabelResultColor(LIGHT_RED_RESULT_COLOR,str(i+1),str(row_result_list[0]))
        elif color_opposite[i] == "1":
            ChangeLabelResultColor(LIGHT_WHITE_RESULT_COLOR,str(i+1),str(row_result_list[0]))
        else: 
            ChangeLabelResultColor(BLACK_COLOR,str(i+1),str(row_result_list[0]))
            
    count_value_inList = 0      
    for i in range(len(list_color_ToCheck)):
        if list_color_ToCheck[i] == EnterColor_list[i]:
            count_value_inList = count_value_inList + 1
            
    count_round.append("One time")
    
    #handle the condition to display a message to the player
    
    if len(count_round) < 10 and count_value_inList != 4:
        score = score_list[0]
        Decrease_score(str(score))
        score_list.pop(0)
    
    if count_value_inList == 4:
        You_win_label()
        TheEndNoti()
    
    if len(count_round) == 10 and count_value_inList != 4:  
        You_lose_label()
        TheEndNoti()
    
    # Handle list to run program not error and fit condition
    row_result_list.pop(0)
    color_opposite_no_number.clear()           
    color_opposite.clear()
    EnterColor_list.clear()
        
def ChangeLabelColor(bg_color):
    name = "Label" + list_label[0] + "_r"+ list_row_label[0]
    name_new = globals()[name]
    name_new['bg'] = bg_color
    EnterColor_list.append(bg_color)
    
    if len(EnterColor_list) == 4:
        Turn_LightResult()
    list_label.pop(0)
    list_row_label.pop(0)
# Use to setup Button click color (above program) to built 8 button click on color
SetButtonClickOnColor(JADE_COLOR,340,200)
SetButtonClickOnColor(GREEN_COLOR,340,240)
SetButtonClickOnColor(YELLOW_COLOR,340,280)
SetButtonClickOnColor(BLUE_COLOR,340,320)
SetButtonClickOnColor(RED_COLOR,340,360)
SetButtonClickOnColor(PINK_COLOR,340,400)
SetButtonClickOnColor(ORANGE_COLOR,340,440)
SetButtonClickOnColor(PURPLE_COLOR,340,480)


#label 1
Label1_r1 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label1_r1.grid(row=2, column=0, sticky="nwse",padx= 10)
Label2_r1 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label2_r1.grid(row=2, column=1, sticky="nwse",padx= 10)
Label3_r1 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label3_r1.grid(row=2, column=2, sticky="nwse",padx= 10)
Label4_r1 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label4_r1.grid(row=2, column=3, sticky="nwse",padx= 10)

#label 2 
Label1_r2 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label1_r2.grid(row=4, column=0, sticky="nwse",padx= 10)
Label2_r2 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label2_r2.grid(row=4, column=1, sticky="nwse",padx= 10)
Label3_r2 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label3_r2.grid(row=4, column=2, sticky="nwse",padx= 10)
Label4_r2 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label4_r2.grid(row=4, column=3, sticky="nwse",padx= 10)

#label 3
Label1_r3 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label1_r3.grid(row=6, column=0, sticky="nwse",padx= 10)
Label2_r3 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label2_r3.grid(row=6, column=1, sticky="nwse",padx= 10)
Label3_r3 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label3_r3.grid(row=6, column=2, sticky="nwse",padx= 10)
Label4_r3 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label4_r3.grid(row=6, column=3, sticky="nwse",padx= 10)

#label 4
Label1_r4 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label1_r4.grid(row=8, column=0, sticky="nwse",padx= 10)
Label2_r4 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label2_r4.grid(row=8, column=1, sticky="nwse",padx= 10)
Label3_r4 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label3_r4.grid(row=8, column=2, sticky="nwse",padx= 10)
Label4_r4 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label4_r4.grid(row=8, column=3, sticky="nwse",padx= 10)

#label 5
Label1_r5 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label1_r5.grid(row=10, column=0, sticky="nwse",padx= 10)
Label2_r5 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label2_r5.grid(row=10, column=1, sticky="nwse",padx= 10)
Label3_r5 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label3_r5.grid(row=10, column=2, sticky="nwse",padx= 10)
Label4_r5 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label4_r5.grid(row=10, column=3, sticky="nwse",padx= 10)

#label 6
Label1_r6 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label1_r6.grid(row=12, column=0, sticky="nwse",padx= 10)
Label2_r6 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label2_r6.grid(row=12, column=1, sticky="nwse",padx= 10)
Label3_r6 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label3_r6.grid(row=12, column=2, sticky="nwse",padx= 10)
Label4_r6 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label4_r6.grid(row=12, column=3, sticky="nwse",padx= 10)

#label 7
Label1_r7 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label1_r7.grid(row=14, column=0, sticky="nwse",padx= 10)
Label2_r7 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label2_r7.grid(row=14, column=1, sticky="nwse",padx= 10)
Label3_r7 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label3_r7.grid(row=14, column=2, sticky="nwse",padx= 10)
Label4_r7 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label4_r7.grid(row=14, column=3, sticky="nwse",padx= 10)

#label 8
Label1_r8 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label1_r8.grid(row=16, column=0, sticky="nwse",padx= 10)
Label2_r8 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label2_r8.grid(row=16, column=1, sticky="nwse",padx= 10)
Label3_r8 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label3_r8.grid(row=16, column=2, sticky="nwse",padx= 10)
Label4_r8 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label4_r8.grid(row=16, column=3, sticky="nwse",padx= 10)

#label 9
Label1_r9 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label1_r9.grid(row=18, column=0, sticky="nwse",padx= 10)
Label2_r9 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label2_r9.grid(row=18, column=1, sticky="nwse",padx= 10)
Label3_r9 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label3_r9.grid(row=18, column=2, sticky="nwse",padx= 10)
Label4_r9 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label4_r9.grid(row=18, column=3, sticky="nwse",padx= 10)

#label 10
Label1_r10 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label1_r10.grid(row=20, column=0, sticky="nwse",padx= 10)
Label2_r10 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label2_r10.grid(row=20, column=1, sticky="nwse",padx= 10)
Label3_r10 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label3_r10.grid(row=20, column=2, sticky="nwse",padx= 10)
Label4_r10 = Label(window, bg = BLACK_COLOR, width= 3,borderwidth=2,relief="solid")
Label4_r10.grid(row=20, column=3, sticky="nwse",padx= 10)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=#

# SetLabelResult 1
LabelResult1_r1 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult1_r1.grid(row=2, column=4, padx= 5)
LabelResult2_r1 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult2_r1.grid(row=2, column=5, padx= 5)
LabelResult3_r1 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult3_r1.grid(row=2, column=6, padx= 5)
LabelResult4_r1 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult4_r1.grid(row=2, column=7, padx= 5)

# SetLabelResult 2
LabelResult1_r2 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult1_r2.grid(row=4, column=4, padx= 5)
LabelResult2_r2 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult2_r2.grid(row=4, column=5, padx= 5)
LabelResult3_r2 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult3_r2.grid(row=4, column=6, padx= 5)
LabelResult4_r2 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult4_r2.grid(row=4, column=7, padx= 5)

# SetLabelResult 3
LabelResult1_r3 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult1_r3.grid(row=6, column=4, padx= 5)
LabelResult2_r3 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult2_r3.grid(row=6, column=5, padx= 5)
LabelResult3_r3 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult3_r3.grid(row=6, column=6, padx= 5)
LabelResult4_r3 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult4_r3.grid(row=6, column=7, padx= 5)

# SetLabelResult 4
LabelResult1_r4 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult1_r4.grid(row=8, column=4, padx= 5)
LabelResult2_r4 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult2_r4.grid(row=8, column=5, padx= 5)
LabelResult3_r4 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult3_r4.grid(row=8, column=6, padx= 5)
LabelResult4_r4 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult4_r4.grid(row=8, column=7, padx= 5)

# SetLabelResult 5
LabelResult1_r5 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult1_r5.grid(row=10, column=4, padx= 5)
LabelResult2_r5 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult2_r5.grid(row=10, column=5, padx= 5)
LabelResult3_r5 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult3_r5.grid(row=10, column=6, padx= 5)
LabelResult4_r5 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult4_r5.grid(row=10, column=7, padx= 5)

# SetLabelResult 6
LabelResult1_r6 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult1_r6.grid(row=12, column=4, padx= 5)
LabelResult2_r6 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult2_r6.grid(row=12, column=5, padx= 5)
LabelResult3_r6 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult3_r6.grid(row=12, column=6, padx= 5)
LabelResult4_r6 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult4_r6.grid(row=12, column=7, padx= 5)

# SetLabelResult 7
LabelResult1_r7 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult1_r7.grid(row=14, column=4, padx= 5)
LabelResult2_r7 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult2_r7.grid(row=14, column=5, padx= 5)
LabelResult3_r7 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult3_r7.grid(row=14, column=6, padx= 5)
LabelResult4_r7 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult4_r7.grid(row=14, column=7, padx= 5)

# SetLabelResult 8
LabelResult1_r8 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult1_r8.grid(row=16, column=4, padx= 5)
LabelResult2_r8 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult2_r8.grid(row=16, column=5, padx= 5)
LabelResult3_r8 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult3_r8.grid(row=16, column=6, padx= 5)
LabelResult4_r8 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult4_r8.grid(row=16, column=7, padx= 5)

# SetLabelResult 9
LabelResult1_r9 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult1_r9.grid(row=18, column=4, padx= 5)
LabelResult2_r9 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult2_r9.grid(row=18, column=5, padx= 5)
LabelResult3_r9 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult3_r9.grid(row=18, column=6, padx= 5)
LabelResult4_r9 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult4_r9.grid(row=18, column=7, padx= 5)

# SetLabelResult 10
LabelResult1_r10 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult1_r10.grid(row=20, column=4, padx= 5)
LabelResult2_r10 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult2_r10.grid(row=20, column=5, padx= 5)
LabelResult3_r10 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult3_r10.grid(row=20, column=6, padx= 5)
LabelResult4_r10 = Label(window, bg = GRAY_COLOR, width= 2,height=1)
LabelResult4_r10.grid(row=20, column=7, padx= 5)

#It wil be called when player press on X button to open notification(show key)
def key_open():
    the_end_label.place(x  = 30, y = 220)
    key_label.place(x  = 30, y = 220)
    color_result_1.place(x  = 90 , y = 320)
    color_result_2.place(x  = 156 , y = 320)
    color_result_3.place(x  = 220 , y = 320)
    color_result_4.place(x  = 285 , y = 320)
    X_button.place(x=333,y=225)
    
the_end_label = Label(window,text = "The End",font = ("Terminal",30),padx=20,pady=50,width=10 ,borderwidth=3,relief="solid",bg = LIGHT_WHITE_RESULT_COLOR)
key_label = Label(window,text = "Key",font = ("Terminal",30),padx=20,pady=50,width=10 ,borderwidth=3,relief="solid",bg = LIGHT_WHITE_RESULT_COLOR)
color_result_1 = Label(window, bg = list_color_ToCheck[0], width= 5,height=2,borderwidth=2,relief="solid")
color_result_2 = Label(window, bg = list_color_ToCheck[1], width= 5,height=2,borderwidth=2,relief="solid")
color_result_3 = Label(window, bg = list_color_ToCheck[2], width= 5,height=2,borderwidth=2,relief="solid")
color_result_4 = Label(window, bg = list_color_ToCheck[3], width= 5,height=2,borderwidth=2,relief="solid")

#It wil be called when player press on X button to close notification(show key)
def key_close(X_button):
    the_end_label.place_forget()
    key_label.place_forget()
    color_result_1.place_forget()
    color_result_2.place_forget()
    color_result_3.place_forget()
    color_result_4.place_forget()
    X_button.place_forget()

# set function buttons

X_button = Button(window,text = "X",bg = LIGHT_WHITE_RESULT_COLOR,font = ("Time new romance",15),fg = BLACK_COLOR,pady=2,padx=5,command=lambda:key_close(X_button))
Button_key= Button(window, text = "Key",bg = BLACK_COLOR, fg = LIGHT_WHITE_RESULT_COLOR, font = ("Terminal",11),pady = 7 ,width=6,command=lambda : key_open()).place(x  =335, y = 130)
Button_music = Button(window, text = " Music",bg = BLACK_COLOR, fg = LIGHT_WHITE_RESULT_COLOR, font = ("Terminal",11),pady = 7 ,width=6,command=lambda : play_music()).place(x  =335, y = 50)
Button_stop_music = Button(window, text = "0Music",bg = BLACK_COLOR, fg = LIGHT_WHITE_RESULT_COLOR, font = ("Terminal",11),pady = 7 ,width=6,command =lambda:stop_music()).place(x  =335, y = 90)
Label_welcome = Label(window, text = "Welcome to MasterMind Game",bg = WINDOW_COLOR, fg = BLUE_COLOR, font = ("VNI-Park",18)).place(x  =10, y = 10)
Label_score = Label(window, text = "Score:",bg = WINDOW_COLOR, fg = BLUE_COLOR, font = ("Terminal",15)).place(x  =50, y = 557)
Label_screen = Label(window,text = "Play",font = ("Terminal",10), width=30, height=2,fg = RED_COLOR,borderwidth=1,relief="solid").place(x =120 , y =555)
# build a bg for app    
Label(window,width= 8, bg =WINDOW_COLOR).grid(row=1, column= 8)

# Setup virtual row for grid function
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.rowconfigure(4,weight=1)
window.rowconfigure(5,weight=1)
window.rowconfigure(6,weight=1)
window.rowconfigure(7,weight=1)
window.rowconfigure(8,weight=1)
window.rowconfigure(9,weight=1)
window.rowconfigure(10,weight=1)
window.rowconfigure(11,weight=1)
window.rowconfigure(12,weight=1)
window.rowconfigure(13,weight=1)
window.rowconfigure(14,weight=1)
window.rowconfigure(15,weight=1)
window.rowconfigure(16,weight=1)
window.rowconfigure(17,weight=1)
window.rowconfigure(18,weight=1)
window.rowconfigure(19,weight=1)
window.rowconfigure(20,weight=1)
window.rowconfigure(21,weight=1)
window.rowconfigure(22,weight=1)
window.rowconfigure(23,weight=1)
window.rowconfigure(24,weight=1)

#Setup virtual column for grid function
window.columnconfigure(0, weight = 2)
window.columnconfigure(1, weight = 2)
window.columnconfigure(2, weight = 2)
window.columnconfigure(3, weight = 2)

window.columnconfigure(4, weight = 1)
window.columnconfigure(5, weight = 1)
window.columnconfigure(6, weight = 1)
window.columnconfigure(7, weight = 1)

window.columnconfigure(8, weight = 2)
# Run tkinter app
window.mainloop()
