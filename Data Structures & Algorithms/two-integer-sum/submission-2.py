class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # O(n)S
        table = {} # num: index

        # O(n)T
        for i, num in enumerate(nums):

            if target - num in table:
                return[table[target - num], i]

            table[num] = i

        return [None, None]
