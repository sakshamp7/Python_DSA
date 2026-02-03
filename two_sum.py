"""
Problem: Two Sum (LeetCode #1)
Difficulty: Easy
Topic: Array, HashMap

Approach:
Use a hashmap to store numbers and their indices.
For each element, check if (target - current) exists in the map.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
