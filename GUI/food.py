import tkinter as tk
from tkinter import *
from tkinter import ttk
from speech_recognition import recognize_speech
from TextOutput import Output_text_and_image
from TextOutput2 import Output_text_and_image2
from VoiceOutput import Output_voice_and_image
from bookmark import bookmark_recommendation
from Category import display_random_image_in_category
import time
import os

root = tk.Tk()

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
frame5 = tk.Frame(root)

frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=0, sticky="nsew")
frame3.grid(row=0, column=0, sticky="nsew")
frame4.grid(row=0, column=0, sticky="nsew")
frame5.grid(row=0, column=0, sticky="nsew")

image1 = tk.PhotoImage(file="man.png")
image2 = tk.PhotoImage(file="woman.png")
image3 = tk.PhotoImage(file="food.png")
image4 = tk.PhotoImage(file="title1.png")

root.title("오늘 뭐 먹지?")
root.wm_iconphoto(False, image3)
root.geometry("440x700") # 가로 * 세로

folder_path = "Final_Project/Team_project/Food"
bookmark_folder = "Final_Project/Team_project/Bookmark"

def openframe(frame):
    frame.tkraise()

introduce = tk.Button(frame2, relief= "solid", text="팀 소개", padx=10, pady=10, command=lambda:[openframe(frame1)])
main = tk.Button(frame1, text="돌아가기", padx=10, pady=10, command=lambda:[openframe(frame2)])
introduce.pack(pady=10)
main.pack()

openframe(frame2)

label_img = Label(frame1, image=image4)
label_img.pack()

gender_select=tk.LabelFrame(frame2, relief='solid', text="성별을 선택하세요", labelanchor='n')
gender_select.pack(ipady=2)

global gender
gender = tk.StringVar() # 여기에 int 형으로 값을 저장한다
man = tk.Radiobutton(gender_select, selectimage=image1, text="남성", variable=gender, value='M', bg="dodgerblue", activebackground="dodgerblue")
woman = tk.Radiobutton(gender_select, selectimage=image2, text="여성", variable=gender, value='F', bg="red", activebackground="red")
man.pack(padx=10)
woman.pack(padx=10)

mode_select=tk.LabelFrame(frame2, relief='solid', text="모드을 선택하세요", labelanchor='n')
mode_select.pack(ipadx=8, ipady=5, pady=10)

# 텍스트 입력 모드 
def textoutput():
    Output_text_and_image(folder_path, bookmark_folder, gender)

def textoutput2():
    Output_text_and_image2(folder_path, bookmark_folder, gender)    
    

func = tk.StringVar()
text = tk.Button(mode_select, text="랜덤 추천 모드", bg = "lightcoral" , command=lambda:[openframe(frame3)])
Label(frame3, width=15, height=1, text="랜덤 추천 모드", bg = "lightcoral").pack(pady=10)
main3 = tk.Button(frame3, text="돌아가기", padx=10, pady=10, command=lambda:[openframe(frame2)])
text.pack(pady=5)
main3.pack()
nowfood = tk.Button(frame3, text="오늘의 음식 추천", command=textoutput)
nowfood.pack(pady= 5)
dailyfood = tk.Button(frame3, text="아침 / 점심 / 저녁 추천", command=textoutput2)
dailyfood.pack(pady= 5)

def voiceoutput():
    Output_voice_and_image(folder_path, bookmark_folder, gender)

# 음성인식 모드
voice = tk.Button(mode_select, text="랜덤 추천 모드 (음성인식)", bg = "darkorange", command=lambda:[openframe(frame4)])
Label(frame4, width=20, height=1, text="랜덤 추천 모드 (음성인식)", bg = "darkorange").pack(pady=10)
main3 = tk.Button(frame4, text="돌아가기", padx=10, pady=10, command=lambda:[openframe(frame2)])
voice.pack(pady=5)
main3.pack()
voicefood = tk.Button(frame4, text="음성인식 시작", command=voiceoutput)
voicefood.pack(pady= 5)


def bookmark_():
    bookmark_recommendation(folder_path, bookmark_folder)

# 북마크 추천 모드
bookmark = tk.Button(mode_select, text="북마크 추천 모드" , bg = "khaki", command=bookmark_)
bookmark.pack(pady=5)

# 카테고리 모드
category = tk.Button(mode_select, text = "카테고리 선택", bg = "lime", command=lambda:[openframe(frame5)])
category.pack(pady=5)
Label(frame5, width=15, height=1, text="카테고리 선택", bg = "lime").pack(pady=10)
main3 = tk.Button(frame5, text="돌아가기", padx=10, pady=10, command=lambda:[openframe(frame2)])
main3.pack()
menubutton=tk.Menubutton(frame5,text="음식 종류 선택", relief="raised", bg = "thistle" , direction="right")
menubutton.pack(pady=10)

a = ["KoreanFood", "ChineseFood", "HealthFood", "FastFood"]           # 콤보 박스에 나타낼 항목 리스트
str = StringVar()
combobox = tk.ttk.Combobox(frame5, textvariable=str, width=10)       # root라는 창에 콤보박스 생성
combobox.config(height=5)           # 높이 설정
combobox.config(values=a)           # 나타낼 항목 리스트(a) 설정
combobox.config(state="readonly")   # 콤보 박스에 사용자가 직접 입력 불가
combobox.set("종류 선택")           # 맨 처음 나타낼 값 설정
combobox.pack()

def camera_():
    os.system(
            "python3 demo.py -i 0")    

# 카메라 인식 모드
camera = tk.Button(mode_select, text="카메라 인식 모드" , bg = "royalblue", command=camera_)
camera.pack(pady=5)

def menu_select():
    category_name = str.get()
    display_random_image_in_category(
        folder_path, category_name, bookmark_folder) # 메뉴선택 함수

recom = tk.Button(frame5, text="선택", command=menu_select)
recom.pack(pady=50)

def quit():
    root.destroy()

exit = tk.Button(frame2, text="종료", command=quit)
exit.pack(pady=20)

root.mainloop()

