import heapq


def min_connection_cost(cable_lengths):
    heapq.heapify(cable_lengths)
    total_cost = 0

    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        cost = first + second
        total_cost += cost
        heapq.heappush(cable_lengths, cost)

    return total_cost


if __name__ == '__main__':
    cable_lengths = [4, 3, 2, 6]
    print("Minimum connection cost:", min_connection_cost(cable_lengths))
