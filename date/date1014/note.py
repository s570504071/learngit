#-*-coding:utf-8-*-
from Tkinter import *
def note():
    n=Tk()
    #指定显示整个框的大小
    n.geometry('720x480')
    n.title('My Note')
    #Label标签，用来显示文字或图片，记得pack之后才能调用
    label=Label(n,text='this is my first note!!!',font='Helvetica -80 bold')
    label.pack()
    #Button按钮，触发命令command
    q=Button(n,text='quit',command=n.quit,bg='red',fg='white')
    q.pack(fill=X,expand=True)
    #scale进度条,范围用from_和to指定，orient指定水平显示进度，command可由lamdba函数定义(自行help(Tkinter.Label.config)
    #缺参数是不行的！！)
    scale=Scale(n,from_=10,to=40,orient=HORIZONTAL,command=lambda no:label.config(font=('Helvetica -{} bold'.format(scale.get()))))
    scale.set(36)
    scale.pack(fill=X,expand=True)
    # Frame框架
    f = Frame(n)
    #Scrollbar滚动条
    fs=Scrollbar(f)
    fs.pack(side=LEFT, fill=Y)
    #Listbox列表框
    l=Listbox(f,font='Helvetica -20 bold')
    l.pack(side=LEFT,fill=Y)
    f.pack()
    mainloop()
if __name__=='__main__':
    note()