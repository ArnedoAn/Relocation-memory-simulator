def fifo(capacidad_memoria, secuencia_paginas):
    memoria_ram = []
    disco = []
    fallos_pagina = 0

    for proceso in secuencia_paginas:
        if proceso not in memoria_ram:
            fallos_pagina += 1
            if len(memoria_ram) < capacidad_memoria:
                memoria_ram.append(proceso)
            else:
                if proceso in disco:
                    disco.remove(proceso)
                disco.append(memoria_ram.pop(0))
                memoria_ram.append(proceso)

        print("Paso {}: Proceso {}, Memoria RAM {}, Disco {}".format(
            secuencia_paginas.index(proceso) + 1, proceso, memoria_ram, disco))

    return fallos_pagina


def lru(capacidad_memoria, secuencia_paginas):
    memoria_ram = []
    disco = []
    fallos_pagina = 0

    for proceso in secuencia_paginas:
        if proceso not in memoria_ram:
            fallos_pagina += 1
            if len(memoria_ram) < capacidad_memoria:
                memoria_ram.append(proceso)
            else:
                disco.append(memoria_ram.pop(0))
                memoria_ram.append(proceso)
        else:
            memoria_ram.remove(proceso)
            memoria_ram.append(proceso)

        print("Paso {}: Proceso {}, Memoria RAM {}, Disco {}".format(
            secuencia_paginas.index(proceso) + 1, proceso, memoria_ram, disco))

    return fallos_pagina


# Ejemplo de uso
capacidad_memoria = 3
secuencia_paginas = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

print("Algoritmo FIFO: {} fallos de página".format(fifo(capacidad_memoria, secuencia_paginas)))
#print("Algoritmo LRU: {} fallos de página".format(lru(capacidad_memoria, secuencia_paginas)))
