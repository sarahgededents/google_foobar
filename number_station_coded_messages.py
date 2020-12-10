import itertools

def solution(l, t):
    assert 0 < len(l) <= 100
    assert 0 <= t <= 250
    cumsums = {cumsum: index for (index, cumsum) in enumerate(itertools.accumulate([0] + l))}
    try:
        return min((cumsums[i], cumsums[t+i] - 1) for i in cumsums if t+i in cumsums)
    except ValueError:
        return -1, -1