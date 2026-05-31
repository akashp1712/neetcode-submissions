from collections import defaultdict

class Solution:
    # O(n * m logm)T | O(n)S
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        table = defaultdict(list) # O(n)S

        # O(n * m logm)T
        for string in strs: # O(n)T

            sorted_string = "".join(sorted(string)) # O(m logm)T
            table[sorted_string].append(string)

        return list(table.values()) # O(n)
        