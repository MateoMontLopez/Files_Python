import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.display = tk.Entry(master, width=30, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Creamos y colocamos los botones en la calculadora
        r = 1
        c = 0
        for b in buttons:
            cmd = lambda x=b: self.click(x)
            tk.Button(master, text=b, width=7, height=2, command=cmd).grid(row=r, column=c)
            c += 1
            if c > 3:
                c = 0
                r += 1

    def click(self, key):
        if key == '=':
            # Realizamos la operación y mostramos el resultado
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        elif key == 'C':
            # Limpiamos la pantalla
            self.display.delete(0, tk.END)
        else:
            # Agregamos el carácter al final del display
            self.display.insert(tk.END, key)

root = tk.Tk()
calc = Calculadora(root)
root.mainloop()
