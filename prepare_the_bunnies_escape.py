def find_distances_to(map_, startx, starty):
    queue = [(startx, starty), None]
    visited = [[False]*len(map_[0]) for _ in range(len(map_))]
    visited[starty][startx] = True

    count = [[-1]*len(map_[0]) for _ in range(len(map_))]

    c = 0
    while queue:
        cur = queue.pop(0)
        if cur is None:
            c += 1
            if queue:
                queue.append(None)
        else:
            col, row = cur
            count[row][col] = c
            if not map_[row][col]:
                for nx, ny in ((col-1, row), (col+1, row), (col, row-1), (col, row+1)):
                    if nx in range(len(map_[0])) and ny in range(len(map_)) and not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((nx, ny))
    return count

def solution(map):
    from_start = find_distances_to(map, 0, 0)
    from_end = find_distances_to(map, len(map[-1]) - 1, len(map) - 1)
    result = 400
    for row in range(len(map)):
        for col in range(len(map[row])):
            if from_start[row][col] != -1 and from_end[row][col] != -1:
                current_dist = from_start[row][col] + from_end[row][col] + 1
                result = min(result, current_dist)
    return result