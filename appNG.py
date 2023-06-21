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


# Ejemplo de uso
secuencia_paginas = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
capacidad_memoria = 3

# fallosF, historialF = reemplazo_pagina_fifo(secuencia_paginas, capacidad_memoria)
# print(f"Algoritmo FIFO: {fallosF} fallos de página")
# for i, (proceso, memoria, disco) in enumerate(historialF):
#     print(f"Paso {i+1}: Proceso {proceso}, Memoria RAM {memoria}, Disco {disco}")

fallosL, historialL = reemplazo_pagina_lru(secuencia_paginas, capacidad_memoria)
print(f"Algoritmo LRU: {fallosL} fallos de página")
for i, (proceso, memoria, disco) in enumerate(historialL):
    print(f"Paso {i+1}: Proceso {proceso}, Memoria RAM {memoria}, Disco {disco}")


