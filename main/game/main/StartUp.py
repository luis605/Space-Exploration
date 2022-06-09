'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from tkinter import *
import tkinter as tk

import threading

import time


class StartUp(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)

    def run(self):
        print("Initializing Startup Popup")

        self.root = tk.Tk()

        self.dot = "."
        self.lastClickX = 0
        self.lastClickY = 0

        self.design()
        self.Refresher()

        self.root.mainloop()


    def close(self):
        self.root.withdraw()
    
    def design(self):
        # Root window
        self.root.title("Space Exploration")
        self.root.geometry('350x350')

        self.root.bind('<Button-1>', self.SaveLastClickPos)
        self.root.bind('<B1-Motion>', self.Dragging)

        self.root.wm_attributes('-type', 'splash')
        self.root.attributes('-alpha',0.8)

        # Labels
        global wait_text_update

        self.Title = tk.Label(self.root, text="\nSpace Exploration", font=("Arial", 25))
        self.Title.pack()

        self.wait_text = tk.Label(self.root, text="\nis loading", font=("Arial", 20))
        self.wait_text.pack()

        self.wait_text_update = tk.Label(self.root, text="\n\nPlease wait...", font=("Arial", 15))
        self.wait_text_update.pack()


        self.spacer = tk.Label(self.root, text="\n\n", font=("Arial", 15))
        self.spacer.pack()


        self.timer = tk.Label(self.root, text="\n\nPlease wait...", font=("Arial", 15))
        self.timer.pack()

    def Refresher(self):
        global timer

        if self.dot == ".":
            self.dot = ".."

        elif self.dot == "..":
            self.dot = "..."
            
        elif self.dot == "...":
            self.dot = "."

        print(self.dot)
    
        self.wait_text_update.configure(text="\n\nPlease wait " + self.dot)

        
        self.timer.configure(text=time.asctime())
        self.root.after(1000, self.Refresher) # every second...



    def SaveLastClickPos(self, event):
        self.lastClickX = event.x
        self.lastClickY = event.y


    def Dragging(self, event):
        x, y = event.x - self.lastClickX + self.root.winfo_x(), event.y - self.lastClickY + self.root.winfo_y()
        self.root.geometry("+%s+%s" % (x , y))

if __name__ == "__main__":
    
    thread1 = StartUp(1)
    thread1.start()
