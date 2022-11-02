


from tkinter import *
import webbrowser
from tkinter import messagebox
root = Tk()


def send():
    send = "You:" + e.get()
    text.insert(END, "\n" + send)
    if (e.get() == "hi"):
        text.insert(END, "\n" + "Bot: hello")
    elif (e.get() == "hello"):
        text.insert(END, "\n" + "Bot: hi")
    elif (e.get() == "how are you"):
        text.insert(END, "\n" + "Bot: I'm fine what about you")
    elif (e.get() == "I'm also good"):
        text.insert(END, "\n" + "Bot: That's great!")
    elif (e.get() == "How can you help me"):
        text.insert(
            END, "\n" + "Bot: I can provide a proper website related to your work within a blink of an eye")
    elif (e.get() == "ok!Good bye"):
        text.insert(END, "\n" + "Bot:Good bye! Nice to meet you")
    elif (e.get() == "I want to access wikipedia"):
        text.insert(END, "\n" + "Bot:Ok", webbrowser.open("wikipedia.com"))
    elif (e.get() == "I want to access google"):
        text.insert(END, "\n" + "Bot:Ok", webbrowser.open("google.com"))
    elif (e.get() == "I want to access Instagram"):
        text.insert(END, "\n" + "Bot:Ok", webbrowser.open("instagram.com"))
    elif (e.get() == "I want to access youtube"):
        text.insert(END, "\n" + "Bot:Ok", webbrowser.open("youtube.com"))
    elif (e.get() == "I want to access facebook"):
        text.insert(END, "\n" + "Bot:Ok", webbrowser.open("facebook.com"))

    elif (e.get() == "I want to access google classroom"):
        text.insert(END, "\n" + "Bot:Ok",
                    webbrowser.open("https://classroom.google.com/u/0"))
    elif (e.get() == "I want to make payment using phonepe"):
        text.insert(END, "\n" + "Bot:Ok", webbrowser.open("phonepe.com"))
    elif (e.get() == "I want to play a game"):
        text.insert(END, "\n" + "Bot:Ok", webbrowser.open("https://poki.com/"))
    elif (e.get() == "I want to use calculator"):

        text.insert(END, "\n" + "Bot:Ok",
                    webbrowser.open("online-calculator.com"))

    elif (e.get() == "I want to order food"):
        text.insert(END, "\n" + "Bot:Ok", webbrowser.open("Swiggy.com"))
    elif (e.get() == "I want to make bill payment"):
        text.insert(END, "\n" + "Bot:Ok", webbrowser.open(
            "https://uppcl.mpower.in/wss/QuickBillPay.htm"))
    else:
        messagebox.showerror(
            "Error!!", "\n " "command not found " " \n " "Try Again..")


text = Text(root, bg="Powder Blue", width=110)
text.grid(row=2, column=0, columnspan=1)
e = Entry(root, width=110)
send = Button(root, text="SEND", bg="light pink", width=10,
              height=3, command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title(" SAURABH'S CHATBOT ")
root.mainloop()
