import random
import time

def exact_set_cover_greedy(universe, subsets):
    used_subsets = []
    subsets = list(sorted(subsets, key=lambda x: len(x), reverse=True))

    def backtrack_greedy(covered, index):
        if covered == universe:
            return True
        if index >= len(subsets):
            return False


        for i in range(index, len(subsets)):
            subset = subsets[i]
            # Verificamos si el subconjunto no comparte elementos ya cubiertos. Operador & es para la interseccion
            if not covered & subset:
                used_subsets.append(subset)
                if backtrack_greedy(covered | subset, i + 1): # Operador | es para la union
                    return True
                used_subsets.pop()
        return False

    if backtrack_greedy(set(), 0):
        return used_subsets
    else:
        return None

if __name__ == "__main__":

    def generate_universe(n):
        return set(range(1, n+1))

    def generate_subsets(n):
        r = random.randint(n, 5*n)
        S = []
        for i in range(1, r):
            l = random.randint(1, n//3)
            s = set()
            while len(s) < l:
                s.add(random.randint(1, n+1))

            S.append(s)

        return S

    U = generate_universe(30)
    S = generate_subsets(30)
    for s in enumerate(S):
        print(s[0], s[1])

    time_inicial_1 = time.time()
    solution = exact_set_cover_greedy(U, S)
    time_final_1 = time.time()

    print("Tiempo de ejecucion de exact_set_cover: ", time_final_1 - time_inicial_1)
    if solution:
        print("Es posible encontrar una cobertura exacta en la solucion 1:")
        for subset in solution:
            print(subset)
    else:
        print("No es posible encontrar una cobertura exacta en 1.")
