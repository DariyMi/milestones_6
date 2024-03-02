from typing import List, Tuple


def find_sum(target: int, li: List[int]) -> Tuple[int, int]:

    n = len(li)
    for i in range(n):
        for j in range(i+1, n):
            if li[i] + li[j] == target:
                return li[i], li[j]
    # Time complexity: O(n^2)
    # Space complexity: O(1)


print(find_sum(3, [1, 2, 3, 4, 5]))
assert find_sum(3, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}


def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:

    all_pairs = {}
    for n in li:
        element = target - n
        if element in all_pairs:
            return all_pairs[element], n
        all_pairs[n] = n

    # Time complexity: O(n)
    # Space complexity: O(n)


print(find_sum_fast(3, [1, 2, 3, 4, 5]))
assert find_sum_fast(3, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}
