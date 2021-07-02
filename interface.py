from tkinter import *
from PIL import ImageTk,Image
import os
from itertools import count, cycle
import subprocess
import webbrowser

#Using absolute file path
here = os.path.dirname(os.path.abspath(__file__))


#Animate splash screen gif
class ImageLabel(Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 50
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


#Intialize main screen
root = Tk()
root.geometry('1024x720+300+100')
root.overrideredirect(True)
root.title('Ono Sendai')
#root.iconbitmap(os.path.join(here, 'samurai.ico'))
#root.iconbitmap('samurai.ico')
root.config(bg='#bb2222')
root.withdraw()


#Initialize start screen
start = Toplevel()
start.overrideredirect(True)
start.geometry('+300+100')
#start.iconbitmap(os.path.join(here, 'samurai.ico'))
img = ImageTk.PhotoImage(Image.open(os.path.join(here, 'coyote.jpg')))
#img = ImageTk.PhotoImage(Image.open('coyote.jpg'))
splash = ImageLabel(start)
splash.pack()
splash.load(os.path.join(here, 'splash.gif'))
#splash.load('splash.gif')

def startup():
    splash.destroy()
    #Create all the start screen stuff
    start.geometry('800x600')
    net = Label(start, image=img)
    net.place(x=0, y=0)
    #Exit app button
    quitpb = Button(start, text='EXIT', fg='black', bg='red', font=('BitBold', 14), command=lambda: start.quit())
    quitpb.place(x=650, y=45, width=100, height=40)
    #Switch to mod screen button
    gotomod = Button(start, text='MOD', fg='black', bg='yellow', font=('BitBold', 14), command=sw_mod)
    gotomod.place(x=420, y=525, width=100, height=40)
    #Open Nexusmods link to dowload mods
    nexuspb = Button(start, text='CYBERSPACE',  fg='black', bg='yellow', font=('BitBold', 14), command=lambda: webbrowser.open_new_tab('https://www.nexusmods.com/cyberpunk2077'))
    nexuspb.place(x=30, y=525, width=170, height=40)


#Switch screens functions
def sw_mod():
    start.withdraw()
    root.deiconify()

def sw_start():
    root.withdraw()
    start.deiconify()


#Switching screen buttons
gotostart = Button(root, text='BACK', fg='black', bg='cyan', font=('BitBold', 14), command=sw_start)
gotostart.grid(row=0, column=0, ipadx=5, ipady=5, padx=(65, 40))


#Quit app button
quitpb = Button(root, text='EXIT', fg='black', bg='cyan', font=('BitBold', 14), command=lambda: root.quit())
quitpb.grid(row=0, column=3, ipadx=5, ipady=5, padx=20)


#Label to get started
mainlabel1 = Label(root, text='', fg='cyan', bg='#BB2222', font=('BitBold', 20))
mainlabel1.grid(row=0, column=1, pady=(60, 40))


#Values for animation 1 is for Jack in and 2 is for Upload
dots = "..."
delta1 = 500 
delay1 = 0
delta2 = 500
delay2 = 0

#Animate Jack in label
def animJI():
    global delta1, delay1
    if mainlabel1.cget('text') != 'Jack In...':
        for i in range(len(dots) + 1):
            s = dots[:i]
            update_label1 = lambda s=s: mainlabel1.config(text= 'Jack In'+ s)
            mainlabel1.after(delay1, update_label1)
            delay1+=delta1
    else:
        mainlabel1.config(text='Jack In')


#Label to install a mod
mainlabel2 = Label(root, text='Upload -\\', fg='cyan', bg='#BB2222', font=('BitBold', 20))
mainlabel2.grid(row=5, column=1, pady=(25, 40))

#Animate Upload label
def animUL():
    global delta2, delay2
    if mainlabel2.cget('text') != 'Upload /-':
        for w in range(3):
            update_label20 = lambda :mainlabel2.config(text='Upload -\\')
            mainlabel2.after(delay2, update_label20)
            delay2+=delta2
            update_label21 = lambda :mainlabel2.config(text='Upload /-')
            mainlabel2.after(delay2, update_label21)
            delay2+=delta2
    else:
        mainlabel1.config(text='Upload -\\')

#Animation runs for this many times
for a in range(100):
    animJI()
    animUL()


#Browse root folder label
rootlabel = Label(root, text='Punch in your Cyberpunk 2077 folder location', fg='white', bg='#BB2222', font=('BitBold', 12))
rootlabel.grid(row=1, column=1, padx=10, pady=5)


#Selected root folder text field 
rootloc = Entry(root, width='50', bg='cyan', borderwidth='2', fg='black', font=('BitBold', 10))
rootloc.grid(row=2, column=1, ipadx=5, ipady=5)


#Browse zip folder label
ziplabel = Label(root, text='Install a mod', fg='white', bg='#BB2222', font=('BitBold', 12))
ziplabel.grid(row=6, column=1, pady=5)


#Selected zip folder text field 
ziploc = Entry(root, width='50', bg='cyan', borderwidth='2', fg='black', font=('BitBold', 10))
ziploc.grid(row=7, column=1, ipadx=5, ipady=5)