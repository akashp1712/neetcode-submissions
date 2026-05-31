class Solution:
    # O(n)S | O(n logk)T
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 1. Find the frequency of all numbers
        frequency = {} # O(n)ST
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1


        unique_elements = list(frequency.keys()) # O(n)ST

        # 2. Use heapq to find top K elements
        heap = [] # O(k)S
        for i in range(0, k):
            num = unique_elements[i]
            heapq.heappush(heap, (frequency[num], num, i)) #O(log k)T
        
        # O(n)T
        for i in range(k, len(unique_elements)):
            num = unique_elements[i]
            if heap and frequency[num] > heap[0][0]:
                heapq.heappop(heap) # O(log k)T
                heapq.heappush(heap, (frequency[num], num, i)) # O(log k)T

        return [item[1] for item in heap]

        



