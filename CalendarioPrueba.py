from tkinter import *
from tkcalendar import *
from gtts import gTTS
import os

#uso de la libreria Tkinter
root = Tk()
root.title("Calendario")
root.geometry("500x500")
root.config(bg="black")

cal = Calendar(root, select="day", year=2023, month=2, day=21)
cal.pack(pady=20, fill="both", expand="yes")

def date():
    Labelf.config(bg= "white", textvariable=audio)

def sound():
    text = Labelf
    lenguaje = 'es-es'
    speech = gTTS(text = text, lang = lenguaje, slow = False)
    speech.save("fecha.mp3")
    os.system("start fecha.mp3")

btnt = Button(root, text="FECHA", command=date)
btnt.pack(pady=10)

audio = StringVar()
Labelf = Label(root, textvariable="")
Labelf.config(bg="black")
Labelf.pack(pady=10)
audio.set("Fecha de hoy " + cal.get_date())

btna = Button(root, text="AUDIO", command=sound)
btna.pack(pady=10)

root.mainloop()
