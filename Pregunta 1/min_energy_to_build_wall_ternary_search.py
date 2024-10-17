import bisect

def min_energy_to_build_wall_ternary_search(heights, c, d, m):
    n = len(heights)
    heights.sort()
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + heights[i]

    min_height = heights[0]
    max_height = heights[-1]

    def compute_cost(H):
        pos = bisect.bisect_left(heights, H)
        build_needed = H * pos - prefix_sums[pos]
        destroy_needed = prefix_sums[n] - prefix_sums[pos] - H * (n - pos)
        if m < c + d:
            x = min(build_needed, destroy_needed)
            cost = x * m + (build_needed - x) * c + (destroy_needed - x) * d
        else:
            cost = build_needed * c + destroy_needed * d
        return cost

    left = min_height
    right = max_height
    min_cost = compute_cost(heights[0])
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        cost1 = compute_cost(mid1)
        cost2 = compute_cost(mid2)
        min_cost = min(min_cost, cost1, cost2)
        if cost1 < cost2:
            right = mid2 - 1
        else:
            left = mid1 + 1
    return min_cost



print("Busqueda ternaria")
heights = [5, 3, 4, 6, 3]
c = 2
d = 3
m = 1

energia_minima = min_energy_to_build_wall_ternary_search(heights, c, d, m)
print(f"Energia minima: {energia_minima}")  # Energia minima: 5

heights = [8, 8, 1, 8, 3, 8, 0, 8]
c = 10
d = 10
m = 19

energia_minima = min_energy_to_build_wall_ternary_search(heights, c, d, m)
print(f"Energia minima: {energia_minima}")  # Energia minima: 200

heights = [1, 3, 2, 2, 5, 1, 3, 1, 4, 5]
c = 3
d = 1
m = 2

energia_minima = min_energy_to_build_wall_ternary_search(heights, c, d, m)
print(f"Energia minima: {energia_minima}")  # Energia minima: 13
