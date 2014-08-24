#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import math
from PIL import Image, ImageTk

fields = ('Sample Count Time (min)', 'Bkg Count Rate (cpm)', 'Bkg Count Time (min)', 'Efficiency (%)', 'Sample Amount (ea)', 'Well Known Bkg MDA (dpm)', 'Paired Bkg MDA (dpm)')

def mda(entries):
   try:
      st = float(entries['Sample Count Time (min)'].get())
      br = float(entries['Bkg Count Rate (cpm)'].get())
      bt = float(entries['Bkg Count Time (min)'].get())
      eff = float(entries['Efficiency (%)'].get())
      sa = float(entries['Sample Amount (ea)'].get())
      wkmda = ((1.645**2 / st) + 3.29 * math.sqrt((br / st) + (br / bt))) / ((eff / 100) * sa)
      wkmda = ("%8.2f" % wkmda).strip()
      entries['Well Known Bkg MDA (dpm)'].delete(0,END)
      entries['Well Known Bkg MDA (dpm)'].insert(0, wkmda)
      pmda = ((1.645**2 / st) + 4.65 * math.sqrt((br / st) + (br / bt))) / ((eff / 100) * sa)
      pmda = ("%8.2f" % pmda).strip()
      entries['Paired Bkg MDA (dpm)'].delete(0,END)
      entries['Paired Bkg MDA (dpm)'].insert(0, pmda)
   except ValueError:
      tkMessageBox.showerror('Error:', 'Zero or non-numeric values entered. Please fix them!')
   except ZeroDivisionError:
      tkMessageBox.showerror('Error:', 'Zero or non-numeric values entered. Please fix them!')
	
def makeform(root, fields):
   root.title("MDA Calculator v0.2")
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w', font=('arial', 12))
      ent = Entry(row, font=('arial', 12))
      ent.insert(0,"0")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT, padx=10)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries
   
def messageWindow():
   win = Toplevel()
   win.geometry("700x940+400+25")
   win.title('MDA Calculator v0.2 -- Program Info')
#   message = "some kind of text /n/nsome more text"
#   msg = Message(win, text=message)
#   msg.config(font=('arial', 16))
#   msg.pack()
   image = Image.open("testpage.jpg")
   photo = ImageTk.PhotoImage(image)
   label = Label(win, image=photo)
   label.image = photo # keep a reference!
   label.pack()
   Button(win, text='OK', font=('arial',12), command=win.destroy).pack()

if __name__ == '__main__':
   root = Tk()
   root.geometry("400x400+300+300")
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: mda(e)))   
   b1 = Button(root, text='Calculate', font=('arial',12), command=(lambda e=ents: mda(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text ="Info", font=('arial',12), command = messageWindow)
   b2.pack(side=LEFT, padx=5, pady=5)   
   b3 = Button(root, text='Quit', font=('arial',12), command=root.quit)
   b3.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
