from tkinter import *

#def processStart():        #게임시작버튼 클릭 이벤트처리

def processOption():        #설정버튼 클릭 이벤트처리
    window = Tk()
    window.geometry("520x480+0+0")

    lbl0 = Label(window, width=7, text='키설정')

    lbl1 = Label(window, width=12, text='사용자이름')
    lbl2 = Label(window, width=12, text='앞으로가기')
    lbl3 = Label(window, width=12, text='왼쪽으로가기')
    lbl4 = Label(window, width=12, text='뒤로가기')
    lbl5 = Label(window, width=12, text='오른쪽으로가기')
    lbl6 = Label(window, width=12, text='달리기')
    lbl7 = Label(window, width=12, text='앉기')
    lbl8 = Label(window, width=12, text='자유시점')
    lbl9 = Label(window, width=12, text='인벤토리')
    lbl10 = Label(window, width=12, text='점프')
    lbl11 = Label(window, width=12, text='1번무기로교체')
    lbl12 = Label(window, width=12, text='2번무기로교체')
    lbl13 = Label(window, width=12, text='3번무기로교체')
    lbl14 = Label(window, width=12, text='감도')
    lbl15 = Label(window, width=12, text='오른쪽기울이기')
    lbl16 = Label(window, width=12, text='왼쪽기울이기')

    txt1 = Text(window, height=1, width=7)
    txt2 = Text(window, height=1, width=7)
    txt3 = Text(window, height=1, width=7)
    txt4 = Text(window, height=1, width=7)
    txt5 = Text(window, height=1, width=7)
    txt6 = Text(window, height=1, width=7)
    txt7 = Text(window, height=1, width=7)
    txt8 = Text(window, height=1, width=7)
    txt9 = Text(window, height=1, width=7)
    txt10 = Text(window, height=1, width=7)
    txt11 = Text(window, height=1, width=7)
    txt12 = Text(window, height=1, width=7)
    txt13 = Text(window, height=1, width=7)
    txt14 = Text(window, height=1, width=7)
    txt15 = Text(window, height=1, width=7)
    txt16 = Text(window, height=1, width=7)


    lbl17 = Label(window, width=13, text='마우스감도조절')
    bar1 = Scale(window, orient='horizontal', length=450)
    btn3 = Button(window, width=13, text='저장')
    btn4 = Button(window, width=13, text='취소')

    lbl0.place(x=10, y=10)
    lbl1.place(x=60, y=50)
    txt1.place(x=150, y=53)
    lbl2.place(x=60, y=80)
    txt2.place(x=150, y=83)
    lbl3.place(x=60, y=110)
    txt3.place(x=150, y=113)
    lbl4.place(x=60, y=140)
    txt4.place(x=150, y=143)
    lbl5.place(x=60, y=170)
    txt5.place(x=150, y=173)
    lbl6.place(x=60, y=200)
    txt6.place(x=150, y=203)
    lbl7.place(x=60, y=230)
    txt7.place(x=150, y=233)
    lbl8.place(x=60, y=260)
    txt8.place(x=150, y=263)

    lbl9.place(x=270, y=50)
    txt9.place(x=360, y=53)
    lbl10.place(x=270, y=80)
    txt10.place(x=360, y=83)
    lbl11.place(x=270, y=110)
    txt11.place(x=360, y=113)
    lbl12.place(x=270, y=140)
    txt12.place(x=360, y=143)
    lbl13.place(x=270, y=170)
    txt13.place(x=360, y=173)
    lbl14.place(x=270, y=200)
    txt14.place(x=360, y=203)
    lbl15.place(x=270, y=230)
    txt15.place(x=360, y=233)
    lbl16.place(x=270, y=260)
    txt16.place(x=360, y=263)

    lbl17.place(x=10, y=315)
    bar1.place(x=30, y=335)

    btn3.place(x=120, y=420)
    btn4.place(x=290, y=420)

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
