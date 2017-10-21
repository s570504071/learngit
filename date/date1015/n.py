#-*-coding:utf-8-*-
from Tkinter import *
#import tkMessageBox
from tkMessageBox import *
def main():
    root=Tk()
    #size
    root.geometry('720x480')
    #title name
    root.title('hi')
    #menu,use m.add_command to show menu you want directly,needn't use add_cascade
    m = Menu(root)
    #start a block :mm
    mm = Menu(m,tearoff=0)
    mm.add_command(label='open',command=root.quit)#can only use label not text!
    mm.add_command(label='copy', command=root.quit)
    mm.add_command(label='save', command=root.quit)
    mm.add_separator()
    mm.add_command(label='quit', command=root.quit)
    #end the block:mm
    m.add_cascade(label='file',menu=mm)

    #new block:mm1
    mm1 = Menu(m, tearoff=0)
    mm1.add_command(label='cut', command=root.quit)
    mm1.add_command(label='paste', command=root.quit)
    mm1.add_command(label='copy', command=root.quit)
    #end
    m.add_cascade(label='edit', menu=mm1)
    #help menu
    mm2 = Menu(m, tearoff=0)
    mm2.add_command(label='help', command=root.quit)
    mm2.add_command(label='author', command=lambda:showinfo('author','by lin'))#use lambda!!
    # end
    m.add_cascade(label='about', menu=mm2)
    #end the menu
    root.config(menu=m)

    #text
    txt=Text(root,undo=True,font='Helvetica -50 bold')
    txt.pack(expand=1,fill=BOTH) #expand and fill is need!
    #滚动条 in txt,       it's useful!!!!!!!!!!!!!
    scl=Scrollbar(txt)
    txt.config(yscrollcommand=scl.set)
    scl.config(command=txt.yview)
    scl.pack(side=RIGHT,fill=Y)
    #-----------
    s=Button(text='save',command=NONE,font='Helvetica -20 bold')
    s.pack()
    #response a new window to show info
    q=Button(text='click me!',bg='red',fg='white',command=lambda :showinfo('choice',message='submit?'))
    q.pack()
    #some data about txt show in bottom
    statusbar = Label(root, text="行 1 column 1", bg="#fff", fg="#00c",  relief=SUNKEN,anchor=E)
    statusbar.pack(side=BOTTOM, fill=X)
    # create a canvas
    frame = Frame(root, width=512, height=512,bg='blue')
    # response a new window to show info
    q = Button(frame,text='click me!', bg='red', fg='white',command=lambda: tkMessageBox.showinfo('choice', message='submit?'))
    q.pack(side=BOTTOM)
    frame.pack(expand=1,fill=BOTH)#important:side,expand and fill(use X,Y or BOTH!!!)
    #frame.bind('<Button-3>',lambda a:m.post(a.x_root,a.y_root))i don't understand yet
    mainloop()
if __name__ =='__main__':
    main()