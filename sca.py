from os import system
from tkinter import messagebox
from tkinter import Tk,Menu,Canvas,BOTH,Button,Label,Entry,IntVar

print('Created By : ')
print('''
    _    _                        _  __        __               _     
   / \  | |__  _ __ ___   ___  __| | \ \      / /_ _  __ _  ___| |__  
  / _ \ | '_ \| '_ ` _ \ / _ \/ _` |  \ \ /\ / / _` |/ _` |/ _ \ '_ \ 
 / ___ \| | | | | | | | |  __/ (_| |   \ V  V / (_| | (_| |  __/ | | |
/_/   \_\_| |_|_| |_| |_|\___|\__,_|    \_/\_/ \__,_|\__, |\___|_| |_|
                                                     |___/           

C	O	P	Y	R	I	G	H	T	©	2019
''')



                        #-- window --
w=Tk()
w.title('CCIST')
ic='ic.ico'
w.iconbitmap(ic)
w.geometry('250x250+200+100')
w.resizable(0,0)


                        #-- functions bar --
def ex():
        w.destroy()

def about():
        messagebox.showinfo('MS','This Program Designed & Created By Ahmed Trojan.')

                        #-- menu bar --
menubar=Menu(w)
options=Menu(menubar,tearoff=0)
options.add_command(label='About Me',command=about)
options.add_command(label='Exit',command=ex)

menubar.add_cascade(label='Properties',menu=options)
w.config(menu=menubar)
                        #-- canvas --
canvas=Canvas(w, width = 300, height = 350, bg = 'white', relief = 'raised')
canvas.pack(fill=BOTH,expand=1)
                        #-- labels --
l1=Label(w,text='H',font=('arial',11,'bold'), bg='white').place(x=60,y=60)
l2=Label(w,text='M',font=('arial',11,'bold'), bg='white').place(x=120,y=60)
l3=Label(w,text='S',font=('arial',11,'bold'), bg='white').place(x=182,y=60)

var1=IntVar()
var2=IntVar()
var3=IntVar()
                        #-- entry --

e1=Entry(w,textvariable=var1,width=3,bg='lightsteelblue2').place(x=60,y=90)
e2=Entry(w,textvariable=var2,width=3,bg='lightsteelblue2').place(x=120,y=90)
e3=Entry(w,textvariable=var3,width=3,bg='lightsteelblue2').place(x=180,y=90)

def run():
        try:
            h=var1.get()
            m=var2.get()
            s=var3.get()
            tot=h+m+s
            if tot==0:
                    messagebox.showerror('MS','Plz Enter one value at least')
            else:
                    t=(h*3600)+(m*60)+s
                    T=str(t)
                    system('shutdown /s /t '+T)
                    messagebox.showinfo('MS',' Ur Computer will shutdown at '+str(h )+' H'+' ...'+str(m )+' M'+' ...'+str(s )+' S')
        except:
                messagebox.showerror('MS','Check ur values')
def stop():
        try:
                system('shutdown /a')
                messagebox.showinfo('MS','Cancelation done')
        except:
                messagebox.showerror('Message','Error Unknown')
def reboot():
        try:
            h=var1.get()
            m=var2.get()
            s=var3.get()
            tot=h+m+s
            if tot==0:
                    messagebox.showerror('MS','Plz Enter one value at least')
            else:
                    t=(h*3600)+(m*60)+s
                    T=str(t)
                    system('shutdown /r /t '+T)
                    messagebox.showinfo('MS',' Ur Computer will shutdown at '+str(h )+' H'+' ...'+str(m )+' M'+' ...'+str(s )+' S')
        except:
              messagebox.showerror('MS','Check ur values')
              
b1=Button(w,text='Run ShutDown',command=run)
b1.place(x=130,y=150)

b2=Button(w,text='Cancel',command=stop,width=24)
b2.place(x=0,y=197)

b3=Button(w,text='Run Restart',command=reboot)
b3.place(x=0,y=150)

b1.config(bg='black',fg='white',font=('Helvetica',11,'bold'))
b2.config(bg='black',fg='white',font=('Helvetica',12,'bold'))
b3.config(bg='black',fg='white',font=('Helvetica',11,'bold'))


w.mainloop()
