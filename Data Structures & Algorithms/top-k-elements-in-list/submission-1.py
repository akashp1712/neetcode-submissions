class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        # Try using Bucket sort algorithm

        # 1. count frequency
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        # 2. Create buckets (n+1) to handle max number
        buckets = [[] for _ in range(len(nums) + 1)]

        # 3. distribute frequency to the buckets
        for num, count in freq.items():
            buckets[count].append(num)

        # 4. find top k numbers
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                k -= 1

                if k == 0:
                    return result

        return result

        