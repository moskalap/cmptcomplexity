from unittest import TestCase

import cmptcomplexity.scripts.solver as slvr
import random
import math

a = 2


class TestSolver(TestCase):
    def test_solve_lin(self):
        x = [random.randint(0, 1000000) for i in range(1000)]
        xlin = [(a + random.uniform(-0.1, 0.1)) * i for i in x]
        s = slvr.Solver(x, xlin)
        res = s.solve()
        self.assertEqual('O(N)', res.complexity)

    def test_solve_x2(self):
        x = [random.randint(0, 1000000) for i in range(1000)]
        xx = [(a + random.uniform(-0.1, 0.1)) * i * i for i in x]
        s = slvr.Solver(x, xx)
        res = s.solve()
        self.assertEqual('O(N^2)', res.complexity)

    def test_solve_log(self):
        x = [random.randint(0, 1000000) for i in range(1000)]
        logx = [(a + random.uniform(-0.1, 0.1)) * math.log2(i) for i in x]
        s = slvr.Solver(x, logx)
        res = s.solve()
        self.assertEqual('O(log N)', res.complexity)

    def test_solve_xlogx(self):
        x = [random.randint(0, 1000000) for i in range(1000)]
        xlogx = [(a + random.uniform(-0.1, 0.1)) * i * math.log2(i) for i in x]
        s = slvr.Solver(x, xlogx)
        res = s.solve()
        self.assertEqual('O(N log N)', res.complexity)
