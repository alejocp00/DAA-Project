import pulp
from utils import generate_subsets, generate_universe
import time
from pulp import PULP_CBC_CMD

def ilp_exact_cover(universe, subsets):
    prob  = pulp.LpProblem("Exact_Cover", pulp.LpMinimize)
    subset_indices = range(len(subsets))

    x = pulp.LpVariable.dicts('x', subset_indices, cat='Binary')

    # prob += pulp.lpSum([x[i] for i in subset_indices])

    for e in universe:
        prob += pulp.lpSum([x[i] for i in subset_indices if e in subsets[i]]) == 1

    prob.solve(PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[prob.status] == 'Optimal':
        solution = [subsets[i] for i in subset_indices if x[i].varValue == 1]
        return solution
    else:
        return None

# Ejemplo de uso:
# U = {1, 2, 3, 4, 5, 6, 7}
# S = [{1, 4, 7}, {1, 4}, {4, 5, 7}, {3, 5, 6}, {2, 3, 6, 7}, {2, 7}]
# result = ilp_exact_cover(U, S)
# if result:
#     print("Solución exacta encontrada mediante PLE:")
#     for subset in result:
#         print(subset)
# else:
#     print("No se encontró una solución exacta.")

U = generate_universe(30)
print(f"Universo \n{U}\n")
S = generate_subsets(30, 5) # Se generaran entre 30 y 5*30 subconjuntos de tamaño random
print("Subconjuntos")
for s in enumerate(S):
    print(s[0], s[1])

time_inicial_1 = time.time()
solution = ilp_exact_cover(U, S)
time_final_1 = time.time()

print("Tiempo de ejecucion de ilp_exact_cover: ", time_final_1 - time_inicial_1)
if solution:
    print("Es posible encontrar una cobertura exacta:")
    for subset in solution:
        print(subset)
else:
    print("No es posible encontrar una cobertura exacta")