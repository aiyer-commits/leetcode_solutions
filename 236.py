import unittest


def solution():

    return


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = []
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    # print(solution())
    unittest.main()


""" problem
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.



According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""


""" approach
bfs for both nodes, keeping parents in a stack
if both nodes found, iterate through stacks until you find a common parent...
"""

""" pseudocode
stack = [[root]]
p_lineage = None
q_lineage = None
while len(stack) > 0 and (p_lineage == None or q_lineage == None):
 lineage = stack.pop()
 if lineage[-1] == p:
  p_lineage = lineage
 elif lineage[-1] == q:
  q_lineage = lineage
 if node.left:
   left_lineage = lineage + [node.left]
   stack.append(left_lineage)
 if node.right:
   right_lineage = lineage + [node.right]
   stack.append(right_lineage)

if len(q_lineage) != len(p_lineage):
  if len(q_lineage) > len(p_lineage:
   q_lineage = q_lineage[:len(p_lineage)]
  else:
   p_lineage = p_lineage[:len(q_lineage)]

while q_lineage[-1] != p_lineage[-1]:
  q_lineage.pop()
  p_lineage.pop()

return q_lineage[-1] if len(q_lineage) > 0) else None
"""
