import time
from tkinter import *
from tkinter import messagebox
from tkinter import Canvas


def bix():
    global var
    
    root = Tk()
    
    canvas1 = Canvas(root, width = 300, height = 300)
    canvas1.pack()
    
    box = messagebox.askyesno("Timer","Your life is about to change are you sure? ")
    
    if box == True:
        var = True
        root.destroy()
    else:
        var = True
        root.destroy()

    root.mainloop()

def nix():
    root = Tk()
    
    canvas1 = Canvas(root, width = 300, height = 300)
    canvas1.pack()
    
    box = messagebox.askyesno("Timer","Go have some fun ")
    
    if box == 'yes':
        root.destroy()
    else:
        root.destroy()

    root.mainloop()

def cix():
    global hynix
    
    root = Tk()
    
    canvas1 = Canvas(root, width = 300, height = 300)
    canvas1.pack()
    
    box = messagebox.askyesno("Timer","Do you want to continue")
    
    if box == True:
        hynix = True
        root.destroy()
    else:
        hynix = False
        root.destroy()

    root.mainloop()



def main():
    global count
    count = 0
    bix()
    while var == True:
        time.sleep(1200)
        count = count + 1
        nix()
        time.sleep(300)
        cix()
        if hynix == True:
            continue
        else:
            break
    print("Done")

main()
print(count)


