from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("LANGUAGE TRANSLATOR")
root.geometry("1000x500")
root.config(bg="#F2CCC3")

title_label = Label(root, text="LANGUAGE TRANSLATOR", bg="#F2CCC3", font=("Constantia", 20, "bold"))
title_label.place(relx=0.5, rely=0.1, anchor="center")

enter_text_label = Label(root, text="Enter Text", bg="#F2CCC3", font=("Constantia", 15))
enter_text_label.place(relx=0.05, rely=0.25, anchor="w")

textarea = Text(root, bg="white", font=("Arial", 12, "normal"), height=10, wrap=WORD, width=40, padx=5, pady=5, bd=0)
textarea.place(relx=0.05, rely=0.5, anchor="w")

root.mainloop()