def pairwise(l):
    a, b = iter(l), iter(l)
    next(b, None)
    return zip(a, b)


def prepare(rooms, entrances, exits):
    single_entrance = [0] + [2_000_000 * (i in entrances) for i in range(len(rooms))] + [0]
    single_exit = [0] * (len(rooms) + 2)
    for r in rooms:
        r.insert(0, 0)
        r.append(0)
    for e in exits:
        rooms[e] = [0] * (len(rooms) + 2)
        rooms[e][-1] = 2_000_000
    return [single_entrance] + rooms + [single_exit]


def bfs(rooms):
    queue = [0]
    visited = [i == 0 for i in range(len(rooms))]
    parents = [None] * len(rooms)
    while queue:
        current_room_idx = queue.pop(0)
        current_room = rooms[current_room_idx]
        neighbours = [i for i in range(len(rooms)) if current_room[i]]
        for i in neighbours:
            if not visited[i]:
                queue.append(i)
                parents[i] = current_room_idx
                visited[i] = True
        if len(rooms) - 1 in neighbours:
            break
    path = []
    current = len(rooms) - 1
    while current is not None:
        path.append(current)
        current = parents[current]
    return list(reversed(path)) if path[-1] == 0 else None


def solution(entrances, exits, path):
    rooms = prepare(path, entrances, exits)
    path = bfs(rooms)
    count = 0
    while path is not None:
        path_capacity = min(rooms[from_][to_] for from_, to_ in pairwise(path))
        count += path_capacity
        for from_, to_ in pairwise(path):
            rooms[from_][to_] -= path_capacity
        path = bfs(rooms)
    return count
