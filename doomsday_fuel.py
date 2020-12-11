from fractions import Fraction

def add_matrix(m1, m2):
    return [[a+b for a, b in zip(l1, l2)] for l1, l2 in zip(m1, m2)]

def scale_matrix(m, s):
    return [[s * v for v in l] for l in m]

def substract_matrix(m1, m2):
    return add_matrix(m1, scale_matrix(m2, -1))

def mult_matrix(m, n):
    assert len(m[0]) == len(n)
    mat = []
    for i in range(len(m)):
        line = []
        for j in range(len(n[0])):
            val = 0
            for k in range(len(n)):
                val += m[i][k] * n[k][j]
            line.append(val)
        mat.append(line)
    return mat

def transpose_matrix(m):
    tmatrice = []
    for i in range(len(m)):
        for j in range(len(m)):
            if i == 0:
                tmatrice.append([])
            tmatrice[j].append(m[i][j])
    return tmatrice


def get_minor_matrix(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def get_det(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    det = 0
    for j in range(len(m)):
        det += ((-1)**j)*m[0][j]*get_det(get_minor_matrix(m, 0, j))
    return det

def get_comat(m):
    comat = []
    for i in range(len(m)):
        for j in range(len(m)):
            if i == 0:
                comat.append([])
            comat[i].append((-1)**(i+j)*get_det(get_minor_matrix(m, i, j)))
    return comat

def get_invert(m):
    det = get_det(m)
    if len(m) == 2:
        return scale_matrix([[m[1][1], -m[0][1]], [-m[1][0], m[0][0]]], Fraction(1, det))
    return scale_matrix(transpose_matrix(get_comat(m)), Fraction(1, det))


def select(m, rows, cols):
    return [[m[r][c] for c in cols] for r in rows]

def get_terminals(m):
    return [i for (i, line) in enumerate(m) if not any(line)]

def get_non_terminals(m):
    return [i for (i, line) in enumerate(m) if any(line)]

def get_identity_matrix(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def lcm_(*args):
    n = len(args)
    args = list(args)
    max_num = 0
    for i in range(n):
        if (max_num < args[i]):
            max_num = args[i]
    res = 1
    x = 2
    while (x <= max_num):
        indexes = []
        for j in range(n):
            if (args[j] % x == 0):
                indexes.append(j)
        if (len(indexes) >= 2):

            for j in range(len(indexes)):
                args[indexes[j]] = int(args[indexes[j]] / x)
            res = res * x
        else:
            x += 1
    for i in range(n):
        res = res * args[i]
    return res


def solution(m):
    m = [[Fraction(j, sum(i) or 1) for j in i] for i in m]
    nt = get_non_terminals(m)
    t = get_terminals(m)
    if len(t) == len(m):
        return [1, 1]
    Q = select(m, nt, nt)
    R = select(m, nt, t)

    I = get_identity_matrix(len(Q))

    f = get_invert(substract_matrix(I, Q))

    res = mult_matrix(f, R)
    res = res[0]
    lcm = lcm_(*(f.denominator for f in res))
    res = [f.numerator * lcm // f.denominator for f in res]
    res.append(lcm)
    return res