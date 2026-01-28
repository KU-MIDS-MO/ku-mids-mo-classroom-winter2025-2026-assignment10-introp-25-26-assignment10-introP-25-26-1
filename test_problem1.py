import sympy as sp
from problem1 import sol, x, y, r

def test_solutions_satisfy_equations():
    for s in sol:
        assert (2*x**2 + 3*y**2 - r).subs(s).simplify() == sp.S(0)
        assert (y - 2*x - 1).subs(s).simplify() == sp.S(0)

def test_number_of_solutions():
    assert len(sol) == 2
    
