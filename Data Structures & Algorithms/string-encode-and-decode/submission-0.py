class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = []
        deli = "#"

        for string in strs:
            encoded.append(str(len(string)))
            encoded.append(deli)
            encoded.append(string)
        
        print("".join(encoded))
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:

        deli = "#"
        curr = 0
        result = []

        while (curr < len(s)):
            number = []
            while (s[curr] != deli):
                number.append(s[curr])
                curr += 1

            count = int("".join(number))
            result.append(s[curr+1:curr+count+1])

            curr = curr + count + 1
            number = []

        return result


        pass
