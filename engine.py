#BB
import os
from pathlib import Path
from zipfile import ZipFile
from interface import *
import shutil
from pyunpack import Archive
import subprocess
import webbrowser

#Getting all mods list function
def getallmods(rootpath):
    chkroot = False
    global listframe1
    global listframe2
    global listframe3
    while chkroot is False:
        try:
            chkroot = Path(rootpath).exists()
            if chkroot:
                arcmodpath = Path(str(rootpath) + '/archive/pc/mod')
                cetmodpath = Path(str(rootpath) + '/bin/x64/plugins/cyber_engine_tweaks/mods')
                redmodpath = Path(str(rootpath) + '/r6/scripts')

            #Archive Mods
                if arcmodpath.exists():
                    arcmoddir = os.listdir(str(rootpath)+'/archive/pc/mod')
                    #Mod list title
                    listframe1 = LabelFrame(root, text='Archive Mods', fg='white', bg='#BB2222', font=('BitBold', 11))
                    listframe1.grid(row=3, column=1, pady=10)
                    #Installed mods listed
                    global listbox1
                    listbox1 = Listbox(listframe1, width=50, fg='cyan', bg='black', font=('BitBold', 10))
                    listbox1.grid(row=3, column=1, padx=15, pady=10)
                    i=1
                    for mods in arcmoddir:
                        listbox1.insert(i, mods)
                        i+=1

            #CET Mods
                if cetmodpath.exists():
                    cetmoddir = os.listdir(str(rootpath)+'/bin/x64/plugins/cyber_engine_tweaks/mods')
                    #Mod list title
                    listframe2 = LabelFrame(root, text='Cyber Engine Tweaks', fg='white', bg='#BB2222', font=('BitBold', 11))
                    listframe2.grid(row=3, column=1, pady=10)
                    #Installed mods listed
                    global listbox2
                    listbox2 = Listbox(listframe2, width=50, fg='cyan', bg='black', font=('BitBold', 10))
                    j=0
                    for plugins in cetmoddir:
                        listbox2.insert(j, plugins)
                        j+=1

            #Red Mods
                if redmodpath.exists():
                    redmoddir = os.listdir(str(rootpath)+'/r6/scripts')
                    #Mod list title
                    listframe3 = LabelFrame(root, text='Red Scripts', fg='white', bg='#BB2222', font=('BitBold', 11))
                    listframe3.grid(row=3, column=1, pady=10)
                    #Installed mods listed
                    global listbox3
                    listbox3 = Listbox(listframe3, width=50, fg='cyan', bg='black', font=('BitBold', 10))
                    k=1
                    for scripts in redmoddir:
                        if scripts.endswith('.toml'):
                            pass
                        else:
                            listbox3.insert(k, scripts)
                        k+=1

        except FileNotFoundError:
            #Show error message
            messagebox.showwarning('Invalid Location', 'Please select the correct directory')


#Label messages
deletelabel = Label(root, text='Deleted Mods are stored in Cyberpunk 2077/deleted', fg='cyan', bg='#BB2222', font=('BitBold', 11))
installlabel = Label(root, text='Upload Successful!', fg='cyan', bg='#BB2222', font=('BitBold', 11))

#Installing Mods
def unzipmod(zippath, rootpath):
    global deletelabel
    global installlabel
    try:
        Archive(str(zippath)).extractall(rootpath)
        deletelabel.grid_forget()
        installlabel.grid(row=8, column=1, pady=20)
    except FileNotFoundError:
        #Show error message
        messagebox.showwarning('Invalid Location', 'Please select the correct directory')

    
#Browse root folder button
rootpb = Button(root, text='Browse',bg='cyan',fg='black', font=('BitBold', 12), command=lambda: openfolder())
rootpb.grid(row=2, column=2, padx=5, pady=5, ipadx=1, ipady=1)


#Open root folder and list all mods function
def openfolder():
    global rootpath
    #Clear text field
    rootloc.delete(0, END)
    rootpath = filedialog.askdirectory()
    rootloc.insert(0, rootpath)
    savefile = open(r'path_data.txt', 'w')
    savefile.write(rootpath)
    getallmods(rootpath)

    #Creating next button
    nexpb = Button(root, text='>>>', fg='cyan', bg='black', font=('BitBold', 15), command=nexlist)
    nexpb.grid(row=3, column=2, padx=(30, 0), pady=10)
    
    #Creating previous button
    prepb = Button(root, text='<<<', fg='cyan', bg='black', font=('BitBold', 15), command=prelist)
    prepb.grid(row=3, column=0, padx=(40, 15), pady=10)
    
    #Delete mods button
    delpb = Button(root, text='DELETE', fg='cyan', bg='black', font=('BitBold', 13), command=lambda: delmod(rootpath))
    delpb.grid(row=4, column=1, pady=(20, 5), ipadx=2, ipady=2)

    #Lauch game button
    cyberpb = Button(start, text='LAUNCH', fg='black', bg='yellow', font=('BitBold', 14), command=lambda: launch(rootpath))
    cyberpb.place(x=280, y=525, width=120, height=40)
    return rootpath


def launch(location):
    global rootpath
    try:
        subprocess.call([str(location)+'/bin/x64/Cyberpunk2077.exe'], shell=True)
    except NameError:
        #Show error message
        messagebox.showwarning('Hold Up, Choom!', 'You need to jack in first')
    return


#Browse mod zip folder button
zippb = Button(root, text='Browse',bg='cyan',fg='black', font=('BitBold', 12), command=lambda: openzip())
zippb.grid(row=7, column=2, padx=5, pady=5, ipadx=1, ipady=1)


#Open installation zip file function
def openzip():
    global zippath
    global rootpath
    try:
        #Clear text field
        ziploc.delete(0, END)
        zippath = filedialog.askopenfilename()
        ziploc.insert(0, zippath)
        unzipmod(zippath, rootpath)
        return zippath
    except NameError:
        #Show error message
        messagebox.showwarning('Hold Up, Choom!', 'You need to jack in first')


#Call this function first
def gotthis():
    startup()
    if os.path.isfile('path_data.txt'):
        copy = open('path_data.txt','r')
        rootpath = copy.readline()
        rootloc.insert(0, rootpath)
        getallmods(rootpath)

        #Creating next button
        nexpb = Button(root, text='>>>', fg='cyan', bg='black', font=('BitBold', 15), command=nexlist)
        nexpb.grid(row=3, column=2, padx=(30, 0), pady=10)
        
        #Creating previous button
        prepb = Button(root, text='<<<', fg='cyan', bg='black', font=('BitBold', 15), command=prelist)
        prepb.grid(row=3, column=0, padx=(40, 15), pady=10)
        
        #Delete mods button
        delpb = Button(root, text='DELETE', fg='cyan', bg='black', font=('BitBold', 13), command=lambda: delmod(rootpath))
        delpb.grid(row=4, column=1, pady=(20, 5), ipadx=2, ipady=2)

        #Lauch game button
        cyberpb = Button(start, text='LAUNCH', fg='black', bg='yellow', font=('BitBold', 14), command=lambda: launch(rootpath))
        cyberpb.place(x=280, y=525, width=120, height=40)
        return(rootpath)


#Go to previous list function
def prelist():
    global listbox1
    global listbox2
    global listbox3
    global listframe1
    global listframe2
    global listframe3
    global prepb
    global nexpb

    if listbox1.winfo_ismapped():
        prepb = Button(root, text='<<', state=DISABLED)
    if listbox2.winfo_ismapped():
        listbox2.grid_forget()
        listframe2.grid_forget()
        listframe1.grid(row=3, column=1, pady=10)
        listbox1.grid(row=3, column=0, padx=15, pady=10)
    if listbox3.winfo_ismapped():
        listbox3.grid_forget()
        listframe3.grid_forget()
        listframe2.grid(row=3, column=1, pady=10)
        listbox2.grid(row=3, column=0, padx=15, pady=10)

#Go to next list function
def nexlist():
    global listbox1
    global listbox2
    global listbox3
    global listframe1
    global listframe2
    global listframe3
    global prepb
    global nexpb

    if listbox1.winfo_ismapped():
        listbox1.grid_forget()
        listframe1.grid_forget()
        listframe2.grid(row=3, column=1, pady=10)
        listbox2.grid(row=3, column=0, padx=15, pady=10)
    if listbox2.winfo_ismapped():
        listbox2.grid_forget()
        listframe2.grid_forget()
        listframe3.grid(row=3, column=1, pady=10)
        listbox3.grid(row=3, column=0, padx=15, pady=10)
    if listbox3.winfo_ismapped():
        nexpb = Button(root, text='>>', state=DISABLED)


#Delete the selected mod function
def delmod(rootpath):
    global listbox1
    global listframe1
    global listframe2
    global listframe3
    global installlabel
    try:
        if listframe1.winfo_ismapped():
            for x in listbox1.curselection():
                if Path(str(rootpath)+'/deleted').exists():
                    shutil.move(str(rootpath)+'/archive/pc/mod/'+str(listbox1.get(x)), str(rootpath)+'/deleted')
                    listbox1.delete(x)
                else:
                    Path(str(rootpath)+'/deleted').mkdir()
        if listframe2.winfo_ismapped():
            for x in listbox2.curselection():
                if Path(str(rootpath)+'/deleted').exists():
                    shutil.move(str(rootpath)+'/bin/x64/plugins/cyber_engine_tweaks/mods/'+str(listbox2.get(x)), str(rootpath)+'/deleted')
                    listbox2.delete(x)
                else:
                    Path(str(rootpath)+'/deleted').mkdir()
        if listframe3.winfo_ismapped():
            for x in listbox3.curselection():
                if Path(str(rootpath)+'/deleted').exists():
                    shutil.move(str(rootpath)+'/r6/scripts/'+str(listbox3.get(x)), str(rootpath)+'/deleted')
                    listbox3.delete(x)
                else:
                    Path(str(rootpath)+'/deleted').mkdir()
        installlabel.grid_forget()
        deletelabel.grid(row=8, column=1, pady=20)
    except NameError:
        #Show error message
        messagebox.showwarning('Hold Up, Choom!', 'You need to jack in first')
    return


#Run the app
start.after(2800, gotthis)
mainloop()