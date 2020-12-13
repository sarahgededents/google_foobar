import itertools

def solution(num_buns, num_required):
    bunnies = [[] for _ in range(num_buns)]
    if num_required == 0:
        return bunnies
    num_keys_per_bunny = num_buns - num_required + 1
    combs = itertools.combinations(bunnies, num_keys_per_bunny)
    for key, comb in enumerate(combs):
        for c in comb:
            c.append(key)
    return sorted(bunnies)