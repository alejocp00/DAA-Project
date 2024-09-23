import random

def generate_universe(n):
    return set(range(1, n + 1))


def generate_subsets(n, a):
    # r representa la cantidad de subconjuntos que se generaran
    r = random.randint(n, a * n)
    S = []
    for i in range(1, r):
        # l representa la longitud de los subconjuntos
        l = random.randint(1, n // 3)
        s = set()
        while len(s) < l:
            s.add(random.randint(1, n))

        S.append(s)

    return S