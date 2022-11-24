'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from tkinter import *



import socket
import os
import threading

class SendReport():
    def __init__(self, message):
        WORKING = True
        SERVER = "127.0.1.1"
        PORT = int("2411")
        FORMAT = 'utf-8'
        DISCONNECT_MESSAGE = "!DISCONNECT"
        ADDR = (SERVER,PORT)

        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect(ADDR)
        print('[CONNECTION] connected successfully')

        def send(msg):
            message = msg.encode(FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(FORMAT)
            send_length += b' '*(2048 - len(send_length))
            client.send(send_length)
            client.send(message)





        print(f"if you want to exit type : {DISCONNECT_MESSAGE}")

##        while WORKING:
        MSG = message
        send(MSG)
##        if MSG == DISCONNECT_MESSAGE:
##            WORKING = False
##            exit()




class ReportError():
    def __init__(self, error):

        self.error = error


        report_window = Tk()

        self.pn = IntVar()
        self.cb = IntVar()

        self.pn_bool = 1
        
        problem_noticed = 1

        # report_window
        report_window.title("Report Error")
        report_window.geometry('500x400')

        try:
            p1 = PhotoImage(file = 'assets/images/error_report/icon.png')
            report_window.iconphoto(True, p1)   
        except:
            pass
        # Information
        lbl = Label(report_window, text="\nHello, we detect an error on our game.\n\nPlease check the buttons you want to tick.\n\nReporting us the error is important to improve your gameplay\n\n")
        lbl.pack()


        def Send():

            print(self.pn)

            if self.pn == "PY_VAR0":
                self.pn_bool = 1
            elif self.pn == "PY_VAR1":
                self.pn_bool= 2
            else:
                print("Problem noticed error")
                
            print(self.error)
            print("Problem Noticed = ", self.pn_bool)

            pn_msg = ", Problem Noticed = "
            self.message_to_send = f'{self.error} {pn_msg} {self.pn_bool}'

##            self.message_to_send = str(self.error, "Problem Noticed = ", str(self.pn_bool))
            print(self.message_to_send)

            SendReport(self.message_to_send)

        

            
            
        # Send Button
        self.send = Button(report_window, text="Send", bg="gray", fg="orange", state=DISABLED, command=Send)
        self.send.place(x=340, y=350)

        def send_update():
            if self.cb.get() == 1:
                self.send['state'] = NORMAL
                self.send['bg'] = "green"
            elif self.cb.get() == 0:
                self.send['state'] = DISABLED
                self.send['bg'] = "gray"
            else:
                messagebox.showerror('Error', 'Something went wrong!')

           


         
#        C1 = Checkbutton(report_window, text = "I noticed the problem", height=5, width = 20, variable=self.pn, onvalue=1, offvalue=0, command=problem_noticed).place(x=150, y=120)

        problem_noticed = False
        C1 = Checkbutton(report_window, text = "The bug was noticeable", variable = problem_noticed, \
                         onvalue = True, offvalue = False, height=5, \
                         width = 20).place(x=150, y=120)

        legal_info = Label(report_window, text="Do you understand that some informations\nof the device and the error will be sent to us?")
        legal_info.place(x = 100, y = 200)



        C2 = Checkbutton(report_window, text="Accept", variable=self.cb, \
                         onvalue=1, offvalue=0, \
                         height=5, \
                         width = 20, \
                         command=send_update)
        C2.place(x=150, y=240)

        # Chat Button
        def Chat():
            SupportChat()
            
        send = Button(report_window, text="Chat", bg="blue", fg="orange", command=Chat)
        send.place(x=100, y=350)

        report_window.mainloop()

class SupportChat():
    pass
if __name__ == "__main__":
    ReportError("oi")
