from subuniverses_greedy import exact_set_cover_greedy
from subuniverses_brute_force import exact_set_cover
from subuniverses_ple import ilp_exact_cover
from utils import generate_subsets, generate_universe
import time

if __name__ == "__main__":
    U = generate_universe(30)
    print(f"Universo \n{U}\n")
    S = generate_subsets(30, 5) # Se generaran entre 30 y 5*30 subconjuntos de tamaño random
    print("Subconjuntos")
    for s in enumerate(S):
        print(s[0], s[1])

    time_inicial_brute = time.time()
    solution_brute = exact_set_cover(U, S)
    time_final_brute = time.time()

    print("Tiempo de ejecucion de exact_set_cover_brute_force: ", time_final_brute - time_inicial_brute)
    if solution_brute:
        print("Es posible encontrar una cobertura exacta en la solucion de fuerza bruta:")
        for subset in solution_brute:
            print(subset)
    else:
        print("No es posible encontrar una cobertura exacta")

    time_inicial_greedy = time.time()
    solution_greedy = exact_set_cover_greedy(U, S)
    time_final_greedy = time.time()
    print("Tiempo de ejecucion de exact_set_cover_greedy: ", time_final_greedy - time_inicial_greedy)
    if solution_greedy:
        print("Es posible encontrar una cobertura exacta en la solucion greedy:")
        for subset in solution_greedy:
            print(subset)
    else:
        print("No es posible encontrar una cobertura exacta")

    time_inicial_ilp = time.time()
    solution_ilp = ilp_exact_cover(U, S)
    time_final_ilp = time.time()
    print("Tiempo de ejecucion de ilp_exact_cover: ", time_final_ilp - time_inicial_ilp)
    if solution_ilp:
        print("Es posible encontrar una cobertura exacta en la solucion ilp:")
        for subset in solution_ilp:
            print(subset)
    else:
        print("No es posible encontrar una cobertura exacta")