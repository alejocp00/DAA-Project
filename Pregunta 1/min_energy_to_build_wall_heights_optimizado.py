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
