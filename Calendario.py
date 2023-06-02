from tkinter import *
from tkcalendar import *

#Se crea un diccionario para almacenar las notas y tareas
notas = {}

#Se crea una funcion para guardar la nota o tarea
def save_note():
    fecha_seleccionada = cal.selection_get()
    anotacion = entry_note.get()
    notas[fecha_seleccionada] = anotacion
    entry_note.delete(0, END)

#Se crea una funcion para ver la nota o tarea guardada
def view_note():
    fecha_seleccionada = cal.selection_get()
    anotacion = notas.get(fecha_seleccionada, "")
    label_note.config(text=anotacion)

#Se crea una ventana
root = Tk()
root.title("Calendario")
root.iconbitmap("C:/Users/ANDRES FERNEY/Desktop/Python/Proyecto/calendar.ico")
root.geometry("500x550")
root.config(bg="black")

#Se crea el calendario para mostrarse en la ventana
cal = Calendar(root, selectmode="day")
cal.bind("<<CalendarSelected>>", lambda event: view_note())
cal.pack(pady=5, fill="both", expand="yes")

#Se crea un Label para darle instrucciones al usuario
label_whatch = Label(root, text="Aca se mostraran las tareas y notas guardadas en la fecha seleccionada", font=('times new roman', 12))
label_whatch.config(bg='black', fg='white')
label_whatch.pack(pady=5)

#Se crea el Label que mostrara la nota o tarea guardada
label_note = Label(root, text="", width=15)
label_note.config(bg='silver', fg='black')
label_note.pack(pady=5)

#Label de indicaciones
label_whatch = Label(root, text="Escriba la nota o tarea a guardar", font=('times new roman', 12))
label_whatch.config(bg='black', fg='white')
label_whatch.pack(pady=5)

#Se crea un Entry para que el usuario digite la nota o tarea que desea guardar
entry_note = Entry(root, width=30, justify='center')
entry_note.config(bg='black', fg='white')
entry_note.pack(pady=5)

#Se crea un boton que guarda la nota o tarea
btnsave = Button(root, text="Guardar", command=save_note)
btnsave.pack(pady=10)

root.mainloop()
