# (c) Roman Menzel

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

fenster = Tk()
fenster.title("Rechner")
fenster.geometry("300x300")
fenster.configure(bg='light blue')

# Funktionen zum Berechnen

def mal():
	try:	
		zahl1 = float(eingabe1.get())
		zahl2 = float(eingabe2.get())
		label_erg.configure(text=(zahl1 * zahl2))
		
	except:
		label_erg.configure(text=("Bitte eine Zahl eingeben!"))

def geteilt():
	try:	
		zahl1 = float(eingabe1.get())
		zahl2 = float(eingabe2.get())
		label_erg.configure(text=(zahl1 / zahl2))
		
	except:
		label_erg.configure(text=("Bitte eine Zahl eingeben!"))

def minus():
	try:	
		zahl1 = float(eingabe1.get())
		zahl2 = float(eingabe2.get())
		label_erg.configure(text=(zahl1 - zahl2))
		
	except:
		label_erg.configure(text=("Bitte eine Zahl eingeben!"))

def plus():
	try:	
		zahl1 = float(eingabe1.get())
		zahl2 = float(eingabe2.get())
		label_erg.configure(text=(zahl1 + zahl2))
		
	except:
		label_erg.configure(text=("Bitte eine Zahl eingeben!"))
		
# Ende der Funktionen zum Berechnen


eingabe1 = Entry()
eingabe1.place(x=0, y=2)

eingabe2 = Entry()
eingabe2.place(x=0, y=50)

# Buttons:

button_plus = Button(text="Plus", command=plus, bg='blue')
button_plus.place(x=0, y=100)

button_minus = Button(text="Minus", command=minus, bg='red')
button_minus.place(x=90, y=100)

button_geteilt = Button(text="Geteilt", command=geteilt, bg='purple')
button_geteilt.place(x=0, y=150)

button_mal = Button(text="Mal", command=mal, bg='yellow')
button_mal.place(x=90, y=150)

# Button Ende

# Labels

label_erg = Label(bg='light blue', font=(15))
label_erg.place(x=90, y=200)

label_wort = Label(text="Ergebnis:", bg='light blue', font=(2))
label_wort.place(x=0, y=200)

# Labels ende 

mainloop()




