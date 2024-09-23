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
