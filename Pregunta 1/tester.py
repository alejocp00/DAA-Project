import time
import random
from functions import min_energy_to_build_wall, min_energy_to_build_wall_optimized, min_energy_to_build_wall_heights, min_energy_to_build_wall_heights_optimized, min_energy_to_build_wall_backtrack, min_energy_to_build_wall_ternary_search

# Importar las soluciones
soluciones = [
    #min_energy_to_build_wall,
    min_energy_to_build_wall_optimized,
    #min_energy_to_build_wall_heights,
    min_energy_to_build_wall_heights_optimized,
    min_energy_to_build_wall_ternary_search
    #min_energy_to_build_wall_backtrack
]

# Generar combinaciones de alturas y costos
def generar_combinaciones(num_combinaciones, max_altura, max_costo):
    combinaciones = []
    for _ in range(num_combinaciones):
        alturas = [random.randint(500000, max_altura) for _ in range(random.randint(100000, 100000))]
        c = random.randint(1, max_costo)
        d = random.randint(1, max_costo)
        m = random.randint(1, max_costo)
        combinaciones.append((alturas, c, d, m))
    return combinaciones

# Probar cada solución con las combinaciones generadas
def probar_soluciones(combinaciones):
    resultados = []
    for i, solucion in enumerate(soluciones):
        tiempos = []
        for alturas, c, d, m in combinaciones:
            start_time = time.time()
            solucion(alturas, c, d, m)
            end_time = time.time()
            tiempos.append(end_time - start_time)
        resultados.append((f'Solución {i+1}', sum(tiempos) / len(tiempos)))
    return resultados

# Generar combinaciones de prueba
combinaciones = generar_combinaciones(1, 1000000, 100)

# Probar las soluciones y mostrar los resultados
resultados = probar_soluciones(combinaciones)
for resultado in resultados:
    print(f'{resultado[0]}: {resultado[1]:.6f} segundos')