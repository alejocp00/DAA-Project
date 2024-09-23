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

        print("h ", h, "Const count ", const_count, "Dest count ", dest_count)

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


print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")

print("Prueba del código Heights")
heights = [5, 3, 4, 6, 3]
c = 2
d = 3
m = 1

energia_minima = min_energy_to_build_wall_heights(heights, c, d, m)
print(f"Energia minima: {energia_minima}")

print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")

heights = [8, 8, 1, 8, 3, 8, 0, 8]
c = 10
d = 10
m = 19

energia_minima = min_energy_to_build_wall_heights(heights, c, d, m)
print(f"Energia minima: {energia_minima}")

print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")

heights = [1, 3, 2, 2, 5, 1, 3, 1, 4, 5]
c = 3
d = 1
m = 2

energia_minima = min_energy_to_build_wall_heights(heights, c, d, m)
print(f"Energia minima: {energia_minima}")
