import functools
import operator

def solve(xs):
    positive_panels = list(panel for panel in xs if panel > 1)
    negative_panels = sorted(panel for panel in xs if panel < 0)
    panels = positive_panels + (negative_panels if not len(negative_panels) % 2 else negative_panels[:-1])
    return str(functools.reduce(operator.mul, panels)) if panels else '0'