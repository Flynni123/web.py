#All for german / Alles auf deutsch

import webbrowser
from tkinter import *

def wikipedia():
    webbrowser.open("https://de.wikipedia.org/")
    quit()

def google():
    webbrowser.open("https://www.google.de/?&hl=de")
    quit()

def localhost():
    webbrowser.open("http://localhost")
    quit()

tk = Tk()
tk.title("Web")
tk.geometry("400x400")

bwikipedia = Button(tk, text="Wikipedia", command=wikipedia)
bgoogle = Button(tk, text="Google", command=google)
blocalhost = Button(tk, text="Localhost", command=localhost)
lnote = Label(tk, text="opens german websites")

blocalhost.pack()
bgoogle.pack()
bwikipedia.pack()
lnote.place(x=0, y=0)

tk.mainloop()
