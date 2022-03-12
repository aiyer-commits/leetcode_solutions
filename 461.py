import unittest


def solution(case):
    n, m = case
    diff_bits = n ^ m
    count = 0
    while diff_bits > 0:
        count += diff_bits & 1
        diff_bits >>= 1
    return count


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [((3, 1), 1), ((1, 4), 2), ((0b101010, 0b010101), 6)]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    # print(solution())
    unittest.main()


""" problem

"""


""" approach

"""

""" pseudocode

"""
