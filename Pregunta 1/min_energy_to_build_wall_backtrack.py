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
