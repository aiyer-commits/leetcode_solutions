import unittest
from collections import Counter


def solution(case):
    tasks, min_break = case
    task_counts = list(Counter(tasks).values())
    m = max(task_counts)
    m_count = task_counts.count(m)
    print(task_counts, m , m_count)
    return max(len(tasks), (m - 1) * (min_break + 1) + m_count)


class TestCase(unittest.TestCase):
    def test_all(self):
        cases = [
            ((["A", "A", "A", "B", "B", "B"], 2), 8),
            ((["A", "A", "A", "B", "B", "B"], 0), 6),
            ((["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2), 16),
            ((["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2), 12),
        ]
        for case, outcome in cases:
            self.assertEqual(solution(case), outcome)
        return


if __name__ == "__main__":
    # print(solution())
    unittest.main()


""" problem
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.



However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.



Return the least number of units of times that the CPU will take to finish all the given tasks.


Example 1:



Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: 

A -> B -> idle -> A -> B -> idle -> A -> B

There is at least 2 units of time between any two same tasks.

Example 2:



Input: tasks = ["A","A","A","B","B","B"], n = 0

Output: 6

Explanation: On this case any permutation of size 6 would work since n = 0.

["A","A","A","B","B","B"]

["A","B","A","B","A","B"]

["B","B","B","A","A","A"]

...

And so on.

Example 3:



Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2

Output: 16

Explanation: 

One possible solution is

A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

 



Constraints:



1 <= task.length <= 104

tasks[i] is upper-case English letter.

The integer n is in the range [0, 100].
"""


""" approach
hashmap to store last time seen
current_time

"""

""" pseudocode

sol(tasks,break_time):
if break_time == 0:
return len(tasks)
scheduled = {}
curr_time = 1
total_hours = 1
for t in tasks:
 if t in scheduled:
  total_hours = scheduled[t] + break_time + 1
  scheduled[t] = total_hours
 else:
  scheduled[t] = curr_time
  curr_time += 1

return total_hours
"""
