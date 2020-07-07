# https://leetcode.com/problems/network-delay-time/
# input ewxample: 
# [[2,1,1],[2,3,1],[3,4,1]]
# 4
# 2


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        #goal 1: the signal travel through all nodes
        #find the shorest time to travel through all nodes
        # Dijkstra (BFS with extra dimension)
        import heapq
        visited = collections.defaultdict(int)
            
        if not times: return -1
        d = collections.defaultdict(list)
        for u, v, w in times:
            d[u].append((v, w))  
        pq = []
        heappush(pq, (0, K)) #time, source

        # strat from node K
        while pq and len(visited)< N:
            global tm
            (tm, source) = heappop(pq)    
            visited[source]=tm
            for target, tm_next in d[source]:               
                if target not in visited: #node not visited
                    heappush(pq, (tm+tm_next, target))

        return tm if len(visited)==N else -1
