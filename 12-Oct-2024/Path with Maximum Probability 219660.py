# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        processed = set()
        distances = defaultdict(list)
        sucProb = [-(log(prob)) if prob != 0 else float("inf") for prob in succProb]
        ans = [float("inf") for _ in range(n)]
        ans[start_node] = 0
        for i in range(len(edges)):
            u, v = edges[i]
            distances[u].append((v, sucProb[i]))
            distances[v].append((u, sucProb[i]))
        heap = [(0, start_node)]

        while heap:
            dist, node = heappop(heap)
            if node in processed:
                continue
            processed.add(node)

            for nod, weight in distances[node]:
                d = weight + dist
                if d < ans[nod]:
                    ans[nod] = d
                    heappush(heap, (d, nod))
        print(ans)
        return e ** -ans[end_node]