from tkinter import *
import sys
print("Who is disgraceful enough to not worship our savior?")
hater1 = sys.stdin.readline()
print("Who else is disgraceful enough to not worship our savior?")
hater2 = sys.stdin.readline()
print("Who else is disgraceful enough to not worship our savior?")
hater3 = sys.stdin.readline()
haters = [hater1, hater2, hater3]
number_of_haters = len(haters)
Subscribe_to_Pewdiepie = Tk()
canvas = Canvas(Subscribe_to_Pewdiepie, width=500, height=500, bd=0)
canvas.pack()
for x in range(0, number_of_haters):
    current_hater = x-1
    txt_x = 250
    txt_y = (150*x) + 50
    message = '%s: "I will subscribe to pewdiepie"'
    canvas.create_text(txt_x, txt_y, text=message % haters[current_hater], fill='red',
                       font=('Times', 15))
