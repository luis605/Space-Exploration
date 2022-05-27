from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('200x80')

def isChecked():
    if cb.get() == 1:
        btn['state'] = NORMAL
        btn.configure(text='Awake!')
    elif cb.get() == 0:
        btn['state'] = DISABLED
        btn.configure(text='Sleeping!')
    else:
        messagebox.showerror('PythonGuides', 'Something went wrong!')

cb = IntVar()

Checkbutton(ws, text="accept T&C", variable=cb, onvalue=1, offvalue=0, command=isChecked).pack()
btn = Button(ws, text='Sleeping!', state=DISABLED, padx=20, pady=5)
btn.pack()

ws.mainloop()
