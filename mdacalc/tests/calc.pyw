#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import math

fields = ('Sample Count Time (min)', 'Bkg Count Rate (cpm)', 'Bkg Count Time (min)', 'Efficiency (%)', 'Sample Amount (ea)', 'Well Known Bkg MDA (dpm)', 'Paired Bkg MDA (dpm)')

def wk_mda(entries):
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
   except ValueError:
      tkMessageBox.showerror('Error:', 'Zero or non-numeric values entered. Please fix them!')
   except ZeroDivisionError:
      tkMessageBox.showerror('Error:', 'Zero or non-numeric values entered. Please fix them!')

def p_mda(entries):
   try:
      st = float(entries['Sample Count Time (min)'].get())
      br = float(entries['Bkg Count Rate (cpm)'].get())
      bt = float(entries['Bkg Count Time (min)'].get())
      eff = float(entries['Efficiency (%)'].get())
      sa = float(entries['Sample Amount (ea)'].get())
      pmda = ((1.645**2 / st) + 4.65 * math.sqrt((br / st) + (br / bt))) / ((eff / 100) * sa)
      pmda = ("%8.2f" % pmda).strip()
      entries['Paired Bkg MDA (dpm)'].delete(0,END)
      entries['Paired Bkg MDA (dpm)'].insert(0, pmda)
   except ValueError:
      tkMessageBox.showerror('Error:', 'Zero or non-numeric values entered. Please fix them!')
   except ZeroDivisionError:
      tkMessageBox.showerror('Error:', 'Zero or non-numeric values entered. Please fix them!')
	
def makeform(root, fields):
   root.title("MDA Calculator v0.1")
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

def combo(e, wk_mda, p_mda):
   wk_mda(e)
   p_mda(e)
   
def messageWindow():
   win = Toplevel()
   win.geometry("500x500+500+200")
   win.title('Program Info')
   message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero.\n\nSed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem. Proin ut ligula vel nunc egestas porttitor. Morbi lectus risus, iaculis vel, suscipit quis, luctus non, massa. Fusce ac turpis quis ligula lacinia aliquet. Mauris ipsum. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. Quisque volutpat condimentum velit."
   msg = Message(win, text=message)
   msg.config(font=('arial', 16))
   msg.pack()   
   Button(win, text='OK', command=win.destroy).pack()

if __name__ == '__main__':
   root = Tk()
   root.geometry("400x400+300+300")
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: combo(e, wk_mda, p_mda)))   
   b1 = Button(root, text='Calculate', command=(lambda e=ents: combo(e, wk_mda, p_mda)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text ="Info", command = messageWindow)
   b2.pack(side=LEFT, padx=5, pady=5)   
   b3 = Button(root, text='Quit', command=root.quit)
   b3.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
