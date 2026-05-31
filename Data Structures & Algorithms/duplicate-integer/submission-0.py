class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        table = set() # O(n)S

        # O(n)T
        for num in nums:
            if num in table:
                return True
            
            table.add(num)

        return False
        