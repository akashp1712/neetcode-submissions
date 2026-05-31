class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(child):

            while parent[child] != child:
                child = parent[child]

            return child


        def union(src, dest):

            parentSrc = find(src)
            parentDest = find(dest)

            if rank[parentSrc] > rank[parentDest]:
                parent[parentDest] = parentSrc
                rank[parentSrc] += rank[parentDest]

            else:
                parent[parentSrc] = parentDest
                rank[parentDest] += rank[parentSrc]

        # 1. union them to a single parent for connected components
        # O(n logn)T
        for src, dest in edges:
            union(src, dest)

        # 2. find parrents of all nodes
        comp = set()

        for i in range(n):
            comp.add(find(i))

        return len(comp)

        
        