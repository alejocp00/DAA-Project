import time
from utils import generate_subsets, generate_universe

def exact_set_cover(universe, subsets):
    used_subsets = []

    def backtrack(covered, index):
        if covered == universe:
            return True
        if index >= len(subsets):
            return False

        for i in range(index, len(subsets)):
            subset = subsets[i]
            # Verificamos si el subconjunto no comparte elementos ya cubiertos. Operador & es para la interseccion
            if not covered & subset:
                used_subsets.append(subset)
                if backtrack(covered | subset, i + 1): # Operador | es para la union
                    return True
                used_subsets.pop()
        return False

    if backtrack(set(), 0):
        return used_subsets
    else:
        return None

if __name__ == "__main__":

    # U = generate_universe(30)
    # print(f"Universo \n{U}\n")
    # S = generate_subsets(30, 5) # Se generaran entre 30 y 5*30 subconjuntos de tamaño random
    # print("Subconjuntos")
    # for s in enumerate(S):
    #     print(s[0], s[1])

    # time_inicial_1 = time.time()
    # solution = exact_set_cover(U, S)
    # time_final_1 = time.time()

    # print("Tiempo de ejecucion de exact_set_cover: ", time_final_1 - time_inicial_1)
    # if solution:
    #     print("Es posible encontrar una cobertura exacta:")
    #     for subset in solution:
    #         print(subset)
    # else:
    #     print("No es posible encontrar una cobertura exacta")

    U = set([1, 2, 3, 4])
    S = [set([1, 2]), set([1, 3]), set([2, 4]), set([3, 4])]
    time_inicial_1 = time.time()
    result = exact_set_cover(U, S)
    time_final_1 = time.time()
    print("Tiempo de ejecucion de exact_set_cover: ", time_final_1 - time_inicial_1)
    if result:
        print("Se encontró una cobertura exacta mediante emparejamiento perfecto:")
        for subset in result:
            print(subset)
    else:
        print("No se encontró una cobertura exacta o el método no es aplicable.")
        
    U_large = set(range(1, 21))
    S_large = [
        set([1, 2, 3]),
        set([4, 5, 6]),
        set([7, 8, 9]),
        set([10, 11, 12]),
        set([13, 14, 15]),
        set([16, 17, 18]),
        set([19, 20]),
        set([1, 4, 7, 10, 13, 16, 19]),
        set([2, 5, 8, 11, 14, 17, 20]),
        set([3, 6, 9, 12, 15, 18])
    ]
    time_inicial_2 = time.time()
    result_large = exact_set_cover(U_large, S_large)
    time_final_2 = time.time()
    print("Tiempo de ejecucion de exact_set_cover para el segundo ejemplo: ", time_final_2 - time_inicial_2)
    if result_large:
        print("Se encontró una cobertura exacta mediante emparejamiento perfecto para el segundo ejemplo:")
        for subset in result_large:
            print(subset)
    else:
        print("No se encontró una cobertura exacta o el método no es aplicable para el segundo ejemplo.")