from tkinter import *
import Control
import DBHelper


def processStart():        #게임시작버튼 클릭 이벤트처리
    global windows
    windows = Tk()
    windows.title("Select Setting")
    windows.geometry("200x300+0+0")

    setlist = DBHelper.list()

    Lbox1 = Listbox(windows, height=12, width=25)
    for item in setlist:
        Lbox1.insert(END,item)
    btn6 = Button(windows, width=13, text='선택', command=lambda: start(Lbox1.curselection()))
    btn7 = Button(windows, width=13, text='취소', command=processsExit)

    Lbox1.activate(0)
    Lbox1.place(x=10,y=10)
    btn6.place(x=40,y=215)
    btn7.place(x=40,y=255)

def start(select):
    if select != ():
        keylist = []
        stack = []
        row = DBHelper.load(select[0] + 1)
        
        for k in range(18):
            keylist.append(row[k+2])
            stack.append(0)
            
        stack.append(0.0)     #keylist에는 없고 stack에만 존재. 마우스의 x와y값.
        stack.append(0.0)
        stack[15] = keylist[15] #mouse sensitivy

        Control.control(keylist, stack)
    

def keyInput(event):
    print("s")

def settingSave(value):
    setlist = []
    setlist.append(txt1.get())
    setlist.append(txt2.get())
    setlist.append(txt3.get())
    setlist.append(txt4.get())
    setlist.append(txt5.get())
    setlist.append(txt6.get())
    setlist.append(txt7.get())
    setlist.append(txt8.get())
    setlist.append(txt9.get())
    setlist.append(txt10.get())
    setlist.append(txt11.get())
    setlist.append(txt12.get())
    setlist.append(txt13.get())
    setlist.append('esc')
    setlist.append(value/50)
    setlist.append(txt15.get())
    setlist.append(txt16.get())

    DBHelper.insert(setlist[0],setlist[1],setlist[2],setlist[3],setlist[4],setlist[5],setlist[6],setlist[7],setlist[8],setlist[9],setlist[10],setlist[11],setlist[12],setlist[13],setlist[14],setlist[15],setlist[16])
    
    processoExit()

def processOption():        #설정버튼 클릭 이벤트처리
    global windowo, txt1, txt2, txt3, txt4, txt5, txt6, txt7, txt8, txt9, txt10, txt11, txt12, txt13, txt14, txt15, txt16
    windowo = Tk()
    windowo.title("Setting")
    windowo.geometry("520x480+0+0")

    lbl0 = Label(windowo, width=7, text='키설정')
    lbl1 = Label(windowo, width=12, text='사용자이름')
    lbl2 = Label(windowo, width=12, text='앞으로가기')
    lbl3 = Label(windowo, width=12, text='왼쪽으로가기')
    lbl4 = Label(windowo, width=12, text='뒤로가기')
    lbl5 = Label(windowo, width=12, text='오른쪽으로가기')
    lbl6 = Label(windowo, width=12, text='달리기')
    lbl7 = Label(windowo, width=12, text='앉기')
    lbl8 = Label(windowo, width=12, text='자유시점')
    lbl9 = Label(windowo, width=12, text='인벤토리')
    lbl10 = Label(windowo, width=12, text='점프')
    lbl11 = Label(windowo, width=12, text='1번무기로교체')
    lbl12 = Label(windowo, width=12, text='2번무기로교체')
    lbl13 = Label(windowo, width=12, text='3번무기로교체')
    lbl15 = Label(windowo, width=12, text='오른쪽기울이기')
    lbl16 = Label(windowo, width=12, text='왼쪽기울이기')

    txt1 = Entry(windowo, width=7)
    txt2 = Entry(windowo, width=7)
    txt3 = Entry(windowo, width=7)
    txt4 = Entry(windowo,  width=7)
    txt5 = Entry(windowo,  width=7)
    txt6 = Entry(windowo, width=7)
    txt7 = Entry(windowo,  width=7)
    txt8 = Entry(windowo, width=7)
    txt9 = Entry(windowo, width=7)
    txt10 = Entry(windowo, width=7)
    txt11 = Entry(windowo,  width=7)
    txt12 = Entry(windowo, width=7)
    txt13 = Entry(windowo, width=7)
    txt15 = Entry(windowo,  width=7)
    txt16 = Entry(windowo,  width=7)

    rows = DBHelper.load(1) #normal

    txt2.insert(0,rows[2])
    txt3.insert(0,rows[3])
    txt4.insert(0,rows[4])
    txt5.insert(0,rows[5])
    txt6.insert(0,rows[6])
    txt7.insert(0,rows[7])
    txt8.insert(0,rows[8])
    txt9.insert(0,rows[9])
    txt10.insert(0,rows[10])
    txt11.insert(0,rows[11])
    txt12.insert(0,rows[12])
    txt13.insert(0,rows[13])
    txt15.insert(0,rows[18])
    txt16.insert(0,rows[19])

    txt2.configure(state='readonly')
    txt3.configure(state='readonly')
    txt4.configure(state='readonly')
    txt5.configure(state='readonly')
    txt6.configure(state='readonly')
    txt7.configure(state='readonly')
    txt8.configure(state='readonly')
    txt9.configure(state='readonly')
    txt10.configure(state='readonly')
    txt11.configure(state='readonly')
    txt12.configure(state='readonly')
    txt13.configure(state='readonly')
    txt15.configure(state='readonly')
    txt16.configure(state='readonly')
    txt2.bind("<Button-1>", keyInput)
    txt3.bind("<Button-1>", keyInput)
    txt4.bind("<Button-1>", keyInput)
    txt5.bind("<Button-1>", keyInput)
    txt6.bind("<Button-1>", keyInput)
    txt7.bind("<Button-1>", keyInput)
    txt8.bind("<Button-1>", keyInput)
    txt9.bind("<Button-1>", keyInput)
    txt10.bind("<Button-1>", keyInput)
    txt11.bind("<Button-1>", keyInput)
    txt12.bind("<Button-1>", keyInput)
    txt13.bind("<Button-1>", keyInput)
    txt15.bind("<Button-1>", keyInput)
    txt16.bind("<Button-1>", keyInput)

    lbl17 = Label(windowo, width=13, text='마우스감도조절')
    bar1 = Scale(windowo, orient='horizontal', length=450)
    bar1.set(50)
    btn3 = Button(windowo, width=13, text='저장', command=lambda: settingSave(bar1.get()))
    btn4 = Button(windowo, width=13, text='취소', command=processoExit)

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
    lbl15.place(x=270, y=200)
    txt15.place(x=360, y=203)
    lbl16.place(x=270, y=230)
    txt16.place(x=360, y=233)

    lbl17.place(x=10, y=315)
    bar1.place(x=30, y=335)

    btn3.place(x=120, y=420)
    btn4.place(x=290, y=420)

def processExit():        #종료버튼 클릭 이벤트처리
    window.destroy()

def processoExit():        #옵션에서 취소버튼 클릭 이벤트처리
    windowo.destroy()

def processsExit():        #설정 선택에서 종료버튼 클릭 이벤트처리
    windows.destroy()

windows = None
windowo = None

window = Tk()
window.title("K/M Trigger")
window.geometry("300x250+0+0")


txt1 = Entry(windowo, width=7)
txt2 = Entry(windowo, width=7)
txt3 = Entry(windowo, width=7)
txt4 = Entry(windowo, width=7)
txt5 = Entry(windowo, width=7)
txt6 = Entry(windowo, width=7)
txt7 = Entry(windowo, width=7)
txt8 = Entry(windowo, width=7)
txt9 = Entry(windowo, width=7)
txt10 = Entry(windowo, width=7)
txt11 = Entry(windowo, width=7)
txt12 = Entry(windowo, width=7)
txt13 = Entry(windowo, width=7)
txt15 = Entry(windowo, width=7)
txt16 = Entry(windowo, width=7)


btn1 = Button(window, width=13, text='게임시작' ,command=processStart)
btn2 = Button(window, width=13, text='설정', command=processOption)
btn3 = Button(window, width=13, text='종료', command=processExit)

btn1.place(x=100,y=60)
btn2.place(x=100,y=110)
btn3.place(x=100,y=160)

window.mainloop()
