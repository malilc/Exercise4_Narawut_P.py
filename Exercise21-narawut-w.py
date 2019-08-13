from tkinter import *
import  math
def leftClickbutton(event):
    total=float(textboxw.get())/math.pow(float(textboxh.get())/100.0,2)
    print(total)
    if(total>=30):
        labelR.configure(text="อ้วนมาก")
    elif(total>=25):
        labelR.configure(text="อ้วน")
    elif (total >= 23):
        labelR.configure(text="น้ำหนักเกิน")
    elif (total >= 18.6):
        labelR.configure(text="น้ำหนักปกติ เหมาะสม")
    elif (total < 18.6):
        labelR.configure(text="ผอมเกินไป")

MainWidow = Tk()
labelh=Label(MainWidow,text="ส่วนสุง (cm.)")
labelh.grid(row=0,column=0)
textboxh=Entry(MainWidow)
textboxh.grid(row=0,column=1)
labelw=Label(MainWidow,text="น้ำหนัก (kg)")
labelw.grid(row=1,column=0)
textboxw=Entry(MainWidow)
textboxw.grid(row=1,column=1)
buttonC=Button(MainWidow,text="คำนวณ")
buttonC.bind('<Button-1>',leftClickbutton)
buttonC.grid(row=2,column=0)
labelR=Label(MainWidow,text="reuslt")
labelR.grid(row=2,column=1)
MainWidow.mainloop()