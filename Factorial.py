import tkinter as tk
from tkinter import messagebox

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def calcular():
    try:
        num = int(entry.get())

        if num < 0:
            messagebox.showerror("Error", "No se permiten números negativos")
            return

        fact = factorial(num)
        resultado.set(f"{num}! = {fact}")

    except ValueError:
        messagebox.showerror("Error", "Introduce un número válido")

# Crear ventana
ventana = tk.Tk()
ventana.title("Factorial de un número")
ventana.geometry("300x200")

# Entrada
tk.Label(ventana, text="Introduce un número").pack()
entry = tk.Entry(ventana)
entry.pack()

# Botón
tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack()

# Ejecutar
ventana.mainloop()