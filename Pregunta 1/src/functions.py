def min_energy_to_build_wall(heights, c, d, m):

    destroy_count = 0
    construct_count = 0
    move_count = 0
    move_blocks = m < c + d
    max_height = max(heights)
    min_height = min(heights)

    while max_height != min_height:

        ceil_count = heights.count(max_height)
        floor_missing_count = heights.count(min_height)

        clean_possible_moves = min(ceil_count, construct_count) if move_blocks else 0
        ceil_clean_cost = (
            m * clean_possible_moves
            + d * (ceil_count - clean_possible_moves)
            - c * clean_possible_moves
        )

        refill_possible_moves = (
            min(floor_missing_count, destroy_count) if move_blocks else 0
        )
        floor_refill_cost = (
            m * refill_possible_moves
            + c * (floor_missing_count - refill_possible_moves)
            - d * refill_possible_moves
        )

        if ceil_clean_cost <= floor_refill_cost:
            # limpiar el techo
            heights = [h - 1 if h == max_height else h for h in heights]
            max_height -= 1
            construct_count -= clean_possible_moves
            move_count += clean_possible_moves
            destroy_count += ceil_count - clean_possible_moves

        else:
            # rellenar el suelo
            heights = [h + 1 if h == min_height else h for h in heights]
            min_height += 1
            destroy_count -= refill_possible_moves
            move_count += refill_possible_moves
            construct_count += floor_missing_count - refill_possible_moves

    cost = destroy_count * d + construct_count * c + move_count * m
    print(
        "Move count ",
        move_count,
        "Destroy count ",
        destroy_count,
        "Construct count ",
        construct_count,
    )
    return cost


print("Versión 1")
heights = [5, 3, 4, 6, 3]
c = 2
d = 3
m = 1

energia_minima = min_energy_to_build_wall(heights, c, d, m)
print(f"Energia minima: {energia_minima}")  # Energia minima: 5

heights = [8, 8, 1, 8, 3, 8, 0, 8]
c = 10
d = 10
m = 19

energia_minima = min_energy_to_build_wall(heights, c, d, m)
print(f"Energia minima: {energia_minima}")  # Energia minima: 200

heights = [1, 3, 2, 2, 5, 1, 3, 1, 4, 5]
c = 3
d = 1
m = 2

energia_minima = min_energy_to_build_wall(heights, c, d, m)
print(f"Energia minima: {energia_minima}")  # Energia minima: 13

def min_energy_to_build_wall_optimized(heights, c, d, m):

    destroy_count = 0
    construct_count = 0
    move_count = 0
    move_blocks = m < c + d
    max_height = max(heights)
    min_height = min(heights)

    row_block_count = [0] * (max_height + 1)

    for h in heights:
        row_block_count[h] += 1

    for i in range(max_height, 0, -1):
        row_block_count[i - 1] += row_block_count[i]

    while max_height != min_height:

        ceil_count = row_block_count[max_height]
        floor_missing_count = len(heights) - row_block_count[min_height + 1]

        clean_possible_moves = min(ceil_count, construct_count) if move_blocks else 0
        ceil_clean_cost = (
            m * clean_possible_moves
            + d * (ceil_count - clean_possible_moves)
            - c * clean_possible_moves
        )
        refill_possible_moves = (
            min(floor_missing_count, destroy_count) if move_blocks else 0
        )
        floor_refill_cost = (
            m * refill_possible_moves
            + c * (floor_missing_count - refill_possible_moves)
            - d * refill_possible_moves
        )

        if ceil_clean_cost <= floor_refill_cost:
            # limpiar el techo
            max_height -= 1
            construct_count -= clean_possible_moves
            move_count += clean_possible_moves
            destroy_count += ceil_count - clean_possible_moves

        else:
            # rellenar el suelo
            min_height += 1
            destroy_count -= refill_possible_moves
            move_count += refill_possible_moves
            construct_count += floor_missing_count - refill_possible_moves

    cost = destroy_count * d + construct_count * c + move_count * m
    print(
        "Move count ",
        move_count,
        "Destroy count ",
        destroy_count,
        "Construct count ",
        construct_count,
    )
    return cost


print("Versión 1 optimizada")
heights = [5, 3, 4, 6, 3]
c = 2
d = 3
m = 1

energia_minima = min_energy_to_build_wall_optimized(heights, c, d, m)
print(f"Energia minima: {energia_minima}")  # Energia minima: 5

heights = [8, 8, 1, 8, 3, 8, 0, 8]
c = 10
d = 10
m = 19

energia_minima = min_energy_to_build_wall_optimized(heights, c, d, m)
print(f"Energia minima: {energia_minima}")  # Energia minima: 200

heights = [1, 3, 2, 2, 5, 1, 3, 1, 4, 5]
c = 3
d = 1
m = 2

energia_minima = min_energy_to_build_wall_optimized(heights, c, d, m)
print(f"Energia minima: {energia_minima}")  # Energia minima: 13


def min_energy_to_build_wall_heights(heights, c, d, m):

    best_cost = 0
    best_combination = []

    for h in range(1, max(heights) + 1):
        const_count = 0
        dest_count = 0
        move_count = 0
        for column in heights:
            if column > h:
                dest_count += column - h
            else:
                const_count += h - column

        if m < c + d:
            move_count = min(dest_count, const_count)
            dest_count -= move_count
            const_count -= move_count

        cost = dest_count * d + const_count * c + move_count * m

        if h == 1 or cost < best_cost:
            best_cost = cost
            best_combination = [move_count, dest_count, const_count]

    print("Best combination ", best_combination)
    return best_cost

print("Prueba del código Heights")
heights = [5, 3, 4, 6, 3]
c = 2
d = 3
m = 1

energia_minima = min_energy_to_build_wall_heights(heights, c, d, m)
print(f"Energia minima: {energia_minima}")

heights = [8, 8, 1, 8, 3, 8, 0, 8]
c = 10
d = 10
m = 19

energia_minima = min_energy_to_build_wall_heights(heights, c, d, m)
print(f"Energia minima: {energia_minima}")

heights = [1, 3, 2, 2, 5, 1, 3, 1, 4, 5]
c = 3
d = 1
m = 2

energia_minima = min_energy_to_build_wall_heights(heights, c, d, m)
print(f"Energia minima: {energia_minima}")


def min_energy_to_build_wall_heights_optimizado(heights, c, d, m):

    best_cost = 0
    best_combination = []
    min_height = min(heights)
    max_height = max(heights)

    block_count = [0] * (max_height + 1)

    for h in heights:
        block_count[h] += 1

    for i in range(max_height, 0, -1):
        block_count[i - 1] += block_count[i]

    block_count[0] = 0
    for i in range(1, max_height):
        block_count[i + 1] += block_count[i]

    for h in range(min_height, max_height + 1):
        const_count = 0
        dest_count = 0
        move_count = 0

        dest_count = block_count[max_height] - block_count[h]
        const_count = len(heights) * h - block_count[h]

        if m < c + d:
            move_count = min(dest_count, const_count)
            dest_count -= move_count
            const_count -= move_count

        cost = dest_count * d + const_count * c + move_count * m

        if h == min_height or cost < best_cost:
            best_cost = cost
            best_combination = [move_count, dest_count, const_count]

    print("Best combination ", best_combination)
    return best_cost

print("Prueba del código Heights optimizado")
heights = [5, 3, 4, 6, 3]
c = 2
d = 3
m = 1

energia_minima = min_energy_to_build_wall_heights_optimizado(heights, c, d, m)
print(f"Energia minima: {energia_minima}")

heights = [8, 8, 1, 8, 3, 8, 0, 8]
c = 10
d = 10
m = 19

energia_minima = min_energy_to_build_wall_heights_optimizado(heights, c, d, m)
print(f"Energia minima: {energia_minima}")

heights = [1, 3, 2, 2, 5, 1, 3, 1, 4, 5]
c = 3
d = 1
m = 2

energia_minima = min_energy_to_build_wall_heights_optimizado(heights, c, d, m)
print(f"Energia minima: {energia_minima}")


def min_energy_to_build_wall_backtrack(heights, c, d, m):
    mask = [0] * len(heights)
    return min_energy_to_build_wall_backtrackR(heights, c, d, m, 0, mask, float("inf"))


def min_energy_to_build_wall_backtrackR(heights, c, d, m, cost, mask, min_energy):

    # poda
    if cost >= min_energy:
        return float("inf")

    if len(set(heights)) == 1:
        min_energy = min(min_energy, cost)
        return cost

    max_height = max(heights)
    min_height = min(heights)
    construct_cost = float("inf")
    destruct_cost = float("inf")
    move_cost = float("inf")

    # aumentar en 1 la altura de una de las columnas más bajas
    min_height_index = heights.index(min_height)
    if mask[min_height_index] != -1:
        last_mask = mask[min_height_index]
        mask[min_height_index] = 1
        heights[min_height_index] += 1
        construct_cost = min_energy_to_build_wall_backtrackR(
            heights, c, d, m, cost + c, mask, min_energy
        )
        mask[min_height_index] = last_mask
        heights[min_height_index] -= 1

    # disminuir en 1 la altura de una de las columnas más altas
    max_height_index = heights.index(max_height)
    if mask[max_height_index] != 1:
        last_mask = mask[max_height_index]
        mask[max_height_index] = -1
        heights[max_height_index] -= 1
        destruct_cost = min_energy_to_build_wall_backtrackR(
            heights, c, d, m, cost + d, mask, min_energy
        )
        mask[max_height_index] = last_mask
        heights[max_height_index] += 1

    # mover un bloque de la columna más alta a la más baja
    if mask[max_height_index] != 1 and mask[min_height_index] != -1:
        last_mask_max = mask[max_height_index]
        last_mask_min = mask[min_height_index]
        mask[max_height_index] = -1
        mask[min_height_index] = 1
        heights[max_height_index] -= 1
        heights[min_height_index] += 1
        move_cost = min_energy_to_build_wall_backtrackR(
            heights, c, d, m, cost + m, mask, min_energy
        )
        mask[max_height_index] = last_mask_max
        mask[min_height_index] = last_mask_min
        heights[max_height_index] += 1
        heights[min_height_index] -= 1

    return min(construct_cost, destruct_cost, move_cost)

print("Prueba del código Backtrack")
heights = [5, 3, 4, 6, 3]
c = 2
d = 3
m = 1

energia_minima = min_energy_to_build_wall_backtrack(heights, c, d, m)
print(f"Energia minima: {energia_minima}")

heights = [1, 3, 2, 2, 5, 1, 3, 1, 4, 5]
c = 3
d = 1
m = 2

energia_minima = min_energy_to_build_wall_backtrack(heights, c, d, m)
print(f"Energia minima: {energia_minima}")
