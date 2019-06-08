from tkinter import *

#def processStart():        #게임시작버튼 클릭 이벤트처리

def processOption():        #설정버튼 클릭 이벤트처리
    window = Tk()
    window.geometry("590x400+0+0")

    lbl0 = Label(window, width=7, text='키설정')
    lbl1 = Label(window, width=7, text='1번프레임')
    lbl2 = Label(window, width=7, text='2번프레임')
    lbl3 = Label(window, width=7, text='3번프레임')
    lbl4 = Label(window, width=7, text='4번프레임')
    lbl5 = Label(window, width=7, text='5번프레임')
    txt1 = Text(window, height=2, width=5)
    txt2 = Text(window, height=2, width=5)
    txt3 = Text(window, height=2, width=5)
    txt4 = Text(window, height=2, width=5)
    txt5 = Text(window, height=2, width=5)
    lbl6 = Label(window, width=13, text='마우스감도조절')
    bar1 = Scale(window, orient='horizontal', length=500)
    btn3 = Button(window, width=13, text='저장')
    btn4 = Button(window, width=13, text='취소')

    lbl0.place(x=30, y=10)
    lbl1.place(x=140, y=50)
    txt1.place(x=147, y=70)
    lbl2.place(x=200, y=50)
    txt2.place(x=207, y=70)
    lbl3.place(x=260, y=50)
    txt3.place(x=267, y=70)
    lbl4.place(x=320, y=50)
    txt4.place(x=327, y=70)
    lbl5.place(x=380, y=50)
    txt5.place(x=387, y=70)

    lbl6.place(x=30, y=200)
    bar1.place(x=30, y=230)

    btn3.place(x=150, y=330)
    btn4.place(x=320, y=330)

def processExit():        #종료버튼 클릭 이벤트처리
    window.destroy()

window = Tk()
window.geometry("300x250+0+0")

btn1 = Button(window, width=13, text='게임시작')
btn2 = Button(window, width=13, text='설정', command=processOption)
btn3 = Button(window, width=13, text='종료', command=processExit)

btn1.place(x=100,y=60)
btn2.place(x=100,y=110)
btn3.place(x=100,y=160)

window.mainloop()