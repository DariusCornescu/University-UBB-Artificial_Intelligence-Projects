from queue import PriorityQueue


def dijkstra(g, s):
    n = len(g["outbound"])
    d = [float('inf')] * n
    f = [-1] * n
    d[s] = 0

    q = PriorityQueue()
    q.put((0, s))
    v = set()

    while not q.empty():
        current_distance, current = q.get()
        if current in v:
            continue
        v.add(current)

        for neighbour in g["outbound"][current]:
            distance = g["outbound"][current][neighbour]
            if d[neighbour] > d[current] + distance:
                d[neighbour] = d[current] + distance
                f[neighbour] = current
                q.put((d[neighbour], neighbour))

    return d, f


def shortest_path(f, number):
    path = []
    while number != -1:
        path.append(number)
        number = f[number]
    path.reverse()
    print(" -> ".join(map(str, path)))


g = {
    "inbound": {
        0: {1: 4, 7: 8},
        1: {0: 4, 2: 8, 7: 11},
        2: {1: 8, 3: 7, 5: 4, 8: 2},
        3: {2: 7, 4: 9, 5: 14},
        4: {3: 9, 5: 10},
        5: {2: 4, 3: 14, 4: 10, 6: 2},
        6: {5: 2, 7: 1, 8: 6},
        7: {0: 8, 6: 1, 8: 7},
        8: {2: 2, 6: 6, 7: 7}
    },
    "outbound": {
        0: {1: 4, 7: 8},
        1: {0: 4, 2: 8, 7: 11},
        2: {1: 8, 3: 7, 5: 4, 8: 2},
        3: {2: 7, 4: 9, 5: 14},
        4: {3: 9, 5: 10},
        5: {2: 4, 3: 14, 4: 10, 6: 2},
        6: {5: 2, 7: 1, 8: 6},
        7: {0: 8, 6: 1, 8: 7},
        8: {2: 2, 6: 6, 7: 7}
    }
}

d, f = dijkstra(g, 0)
for i in range(1, 9):
    print(f"Shortest path to {i}: ", end="")
    shortest_path(f, i)
