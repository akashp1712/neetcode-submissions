from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        table = defaultdict(list)

        for string in strs:

            sorted_string = "".join(sorted(string))
            table[sorted_string].append(string)

        return list(table.values())
        