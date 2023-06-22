import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Algoritmos de reemplazo de página
def reemplazo_pagina_fifo(paginas, capacidad):
    memoria = []
    disco = []
    fallos_pagina = 0
    historial_reemplazo = []  # Lista para almacenar el historial de reemplazo

    for pagina in paginas:
        if pagina not in memoria:
            fallos_pagina += 1
            if len(memoria) < capacidad:
                memoria.append(pagina)
            else:
                if pagina in disco:
                    disco.remove(pagina)
                disco.append(memoria.pop(0))
                memoria.append(pagina)
        
        historial_reemplazo.append((pagina, list(memoria), list(disco)))  # Guardar el proceso y la configuración actual de la memoria en el historial

    return fallos_pagina, historial_reemplazo

def reemplazo_pagina_lru(paginas, capacidad):
    memoria = []
    disco = []
    fallos_pagina = 0
    historial_reemplazo = []  # Lista para almacenar el historial de reemplazo

    for pagina in paginas:
        if pagina not in memoria:
            fallos_pagina += 1
            if len(memoria) < capacidad:
                memoria.append(pagina)
            else:
                if pagina in disco:
                    disco.remove(pagina)
                disco.append(memoria.pop(0))
                memoria.append(pagina)
        else:
            if pagina in disco:
                disco.remove(pagina)
            memoria.remove(pagina)
            memoria.append(pagina)
        
        historial_reemplazo.append((pagina, list(memoria), list(disco)))  # Guardar el proceso y la configuración actual de la memoria en el historial
    
    return fallos_pagina, historial_reemplazo

# Función para generar una animación
def animate(algoritmo, secuencia_paginas, capacidad_memoria):
    if algoritmo == "FIFO":
        fallos, historial = reemplazo_pagina_fifo(secuencia_paginas, capacidad_memoria)
    elif algoritmo == "LRU":
        fallos, historial = reemplazo_pagina_lru(secuencia_paginas, capacidad_memoria)
    else:
        messagebox.showerror("Error", "Algoritmo no válido")
        return

    fig, ax = plt.subplots(figsize=(8, 6))
    plt.title(f"Algoritmo: {algoritmo} | Capacidad de Memoria: {capacidad_memoria}")
    plt.xlabel("Paso")
    plt.ylabel("Memoria")

    def update(i):
        ax.clear()
        ax.axis('off')
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])

        proceso, memoria, disco = historial[i]

        ax.text(0.25, 0.01, f"Proceso: {proceso}", fontsize=12, ha='center')
        ax.text(0.5, 0.42, f"Memoria RAM", fontsize=12, ha='center',weight='bold')
        ax.text(0.7, 0.01, f"Marcos disponibles: {capacidad_memoria}", fontsize=12, ha='center')
        
        # Dibujar la memoria RAM
        ax.add_patch(plt.Rectangle((0.05, 0.1), 0.9, 0.4, facecolor='lightgreen', linewidth=1, edgecolor='black'))

        # Dibujar cuadrados representando los procesos en la Memoria RAM
        for j, p in enumerate(memoria):
            ax.add_patch(plt.Rectangle((0.1 + j * 0.1, 0.26), 0.08, 0.08, facecolor='blue', linewidth=1, edgecolor='black'))
            ax.text(0.14 + j * 0.1, 0.29, str(p), fontsize=10, ha='center', color='white')

        # Dibujar el disco duro
        ax.add_patch(plt.Rectangle((0.05, 0.6), 0.9, 0.4, facecolor='lightblue', linewidth=1, edgecolor='black'))
        ax.text(0.5, 0.92, "Disco Duro", fontsize=12, weight='bold', ha='center')

        # Dibujar los cuadrados representando los procesos en el disco duro
        for j, p in enumerate(disco):
            ax.add_patch(plt.Rectangle((0.1 + j * 0.1, 0.76), 0.08, 0.08, facecolor='red', linewidth=1, edgecolor='black'))
            ax.text(0.14 + j * 0.1, 0.79, str(p), fontsize=10, ha='center', color='white')
        
        def on_animation_finished():
            start_button.config(state="normal")
            messagebox.showinfo("Simulación Terminada", "La simulación ha finalizado.")

        if i == len(historial) - 1:
            ani.event_source.stop()
            on_animation_finished()

    ani = animation.FuncAnimation(fig, update, frames=len(historial), interval=1600)
    ani.event_source.stop()
    plt.show()

# Función para manejar el botón Start
def start_simulation():
    secuencia = input_secuencia.get()
    capacidad = input_capacidad.get() # Maximo de marcos = 8
    algoritmo = dropdown_algoritmo.get()

    if not secuencia or not capacidad:
        messagebox.showerror("Error", "Por favor, ingresa la secuencia de páginas y la capacidad de memoria")
        return

    if int(capacidad) > 8:
        messagebox.showerror("Error", "La capacidad de memoria no puede ser mayor a 8")
        return
    
    try:
        secuencia_paginas = list(map(int, secuencia.split(',')))
        capacidad_memoria = int(capacidad)
        animate(algoritmo, secuencia_paginas, capacidad_memoria)
        #start_button.config(state="disabled")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una secuencia válida y un valor numérico para la capacidad de memoria")
        return

# Crear la ventana principal
window = tk.Tk()
window.title("Simulador de Reemplazo de Páginas")
window.geometry("400x200")

# Crear los widgets
label_secuencia = tk.Label(window, text="Secuencia de páginas (separadas por comas):")
label_secuencia.pack()

input_secuencia = tk.Entry(window, width=30)
input_secuencia.pack()

label_capacidad = tk.Label(window, text="Capacidad de memoria (Máximo 8):")
label_capacidad.pack()

input_capacidad = tk.Entry(window, width=10)
input_capacidad.pack()

label_algoritmo = tk.Label(window, text="Algoritmo de reemplazo:")
label_algoritmo.pack()

dropdown_algoritmo = tk.StringVar(window)
dropdown_algoritmo.set("SELECIONA UN ALGORITMO")

dropdown = tk.OptionMenu(window, dropdown_algoritmo, "FIFO", "LRU")
dropdown.pack()

start_button = tk.Button(window, text="Start", command=start_simulation)
start_button.pack()

# Ejecutar el bucle principal de la ventana
window.mainloop()
