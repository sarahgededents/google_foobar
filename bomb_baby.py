def solution(x, y):
    bomb_amount = 0
    x, y = int(x), int(y)
    while x != 1 and y != 1:
        if y % x == 0:
            return "impossible"
        x, y = min(x, y), max(x, y)
        bomb_amount += y // x
        y = y % x
    bomb_amount += max(x, y) - 1
    return str(bomb_amount)