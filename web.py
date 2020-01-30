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

blocalhost.pack()
bgoogle.pack()
bwikipedia.pack()

tk.mainloop()
