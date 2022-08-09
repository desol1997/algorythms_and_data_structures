# The first line contains the number of items 1 <= n <= 10^3 and knapsack capacity 0 <= W <= 2*10^6.
# Each of the next n lines specifies the cost 0 <= ci <= 2*10^6 and volume 0 <= wi <= 2*10^6.
# Output the maximum cost of parts of items (any part can be separated from each item,
# the cost and volume will decrease proportionally) that fit into the given knapsack,
# with an accuracy of at least three decimal places.

# Sample Input:
# 3 50
# 60 20
# 100 50
# 120 30

# Sample Output:
# 180.000

import heapq
import sys


def fractional_knapsack(knapsack_capacity, values_weights):
    order = [(-v / w, w) for v, w in values_weights]
    heapq.heapify(order)

    acc = 0
    while order and knapsack_capacity:
        v_per_w, w = heapq.heappop(order)
        can_take = min(w, knapsack_capacity)
        acc -= v_per_w * can_take
        knapsack_capacity -= can_take

    return acc


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    values_and_weights = [*reader]
    opt_value = fractional_knapsack(capacity, values_and_weights)
    print(f'{opt_value:.3f}')


if __name__ == '__main__':
    main()
