import itertools
import operator

def solution(l):
    def digits_to_int(digits):
        powers_of_ten = itertools.chain((1,), itertools.accumulate(itertools.repeat(10), operator.mul))
        return sum(d*p for (d, p) in zip(digits, powers_of_ten))

    numbers = (digits_to_int(digits)
               for i in range(1, len(l))
               for comb in itertools.combinations(l, i)
               for digits in itertools.permutations(comb))
    try:
        return max(n for n in numbers if (n % 3) == 0)
    except ValueError:
        return 0