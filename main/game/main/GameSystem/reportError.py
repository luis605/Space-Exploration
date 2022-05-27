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

        # Information
        lbl = Label(report_window, text="Hello, we detect an error on our game.\n\nPlease help us correcting the bug by\nreporting to us that error\n\n Help us understanding the problem with a little quiz")
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
        send = Button(report_window, text="Send", bg="green", fg="orange", state=DISABLED, command=Send)
        send.place(x=340, y=350)

        def send_update():
            if self.cb.get() == 0:
                send['state'] = DISABLED
            elif self.cb.get() == 1:
                send['state'] = NORMAL
                

        def problem_noticed():
            if self.pn.get() == 0:
                problem_noticed = False
            elif self.pn.get() == 1:
                problem_noticed = True


            


         
        C1 = Checkbutton(report_window, text = "I noticed the problem", height=5, width = 20, variable=self.pn, onvalue=1, offvalue=0, command=problem_noticed).place(x=150, y=120)


        legal_info = Label(report_window, text="Do you understand that some informations\nof the device and the error will be sent to us?")
        legal_info.place(x = 100, y = 200)



        Checkbutton(report_window, text="I understand and I accept it", height=5, width = 20, variable=self.cb, onvalue=1, offvalue=0, command=send_update).place(x=150, y=240)




        #C2.place(x=150, y=240)


        report_window.mainloop()

if __name__ == "__main__":
    ReportError("oi")
