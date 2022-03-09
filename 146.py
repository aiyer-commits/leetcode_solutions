import unittest


class DLLNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev_el = None
        self.next_el = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLLNode(), DLLNode()

    def add(self, node):
        node.prev_el = self.head
        node.next_el = self.head.next_el
        self.head.next_el.prev_el = node
        self.head.next_el = node

    def remove(self, node):
        prev_el = node.prev_el
        new_el = node.next_el
        prev_el.next = new_el
        new_el.prev_el = prev_el

    def move_to_head(self, node):
        self.remove(node)
        self.add(node)

    def pop_tail(self):
        res = self.tail.prev_el
        self.remove(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self.move_to_head(node)

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            new_node = DLLNode()
            new_node.key = key
            new_node.value = value
            self.cache[key] = new_node
            self.add(new_node)

            self.size += 1

            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self.move_to_head(node)


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
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.



Implement the LRUCache class:



LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""


""" approach
hashmap to store values
queue to store usage order... 
"""

""" pseudocode
init:
store = {}
last_used = {}
cap = capacity
current_time = 0

get(k):
if k in store:
 last_used[current_time] = k
 current_time += 1
 return store[k]
else:
return -1

put(pair):
k, v = pair
store[k] = v
if current_time - cap in last_used:
 del store[last_used[current_time - cap]]
last_used[current_time] = k
current_time += 1

"""
