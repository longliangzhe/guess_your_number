from tkinter import Tk,Label,Button,Frame,StringVar


root = Tk()
root.title('数字心理感应')
root.geometry('700x500')
root.iconbitmap('heart.ico')


numbers = [[i for i in range(1,32,2)],
           [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31],
           [4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31],
           [8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31],
           [j for j in range(16,32)]]


Label(root,text='数字心理感应',font=('微软雅黑',20)).pack()
l1 = Label(root,text='请从1~31中想一个数字，我将猜出你选择的数字')
l1.pack()
l4 = Label(root)
b4 = Button(root,text='重新开始')
ask_frame = Frame(root)
page = 0
var = StringVar()
var.set(str(numbers[page])[1:-1])
digit = []


def restart():
    global page
    page = 0
    digit.clear()
    l4.pack_forget()
    b4.pack_forget()
    var.set(str(numbers[page])[1:-1])
    play()
b4.config(command=restart)
def answer():
    global digit
    ask_frame.pack_forget()
    bin = ''.join(digit)
    l4.config(text='你想的数字是'+str(int(bin,2))+'，我猜对了吧')
    l4.pack()
    b4.pack()
def yes():
    global page,digit
    digit = ['1'] + digit
    if page == 4:
        answer()
    else:
        page += 1
        var.set(str(numbers[page])[1:-1])
def no():
    global page,digit
    digit = ['0'] + digit
    if page == 4:
        answer()
    else:
        page += 1
        var.set(str(numbers[page])[1:-1])
def play():
    global ask_frame
    b1.pack_forget()
    l1.pack_forget()
    ask_frame = Frame(root)
    l2 = Label(ask_frame,text='你所选择的数字是否在以下数组中？')
    l2.pack()
    l3 = Label(ask_frame,textvariable=var)
    l3.pack()
    b2 = Button(ask_frame,text='在',command=yes)
    b2.pack(side='left')
    b3 = Button(ask_frame,text='不在',command=no)
    b3.pack(side='right')
    ask_frame.pack()
b1 = Button(root,text='开始',command=play)
b1.pack()
Button(root,text='退出',font=('宋体',15),command=root.destroy).pack(side='bottom')
root.mainloop()
