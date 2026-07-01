from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        
        # Step 1: Multi-source BFS to compute distance from nearest thief
        dist = [[-1]*n for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        
        # Step 2: Max heap (Dijkstra-like)
        max_heap = [(-dist[0][0], 0, 0)]  # (negative safeness, r, c)
        visited = [[False]*n for _ in range(n)]
        visited[0][0] = True
        
        while max_heap:
            safe, r, c = heapq.heappop(max_heap)
            safe = -safe
            
            if (r, c) == (n-1, n-1):
                return safe
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    new_safe = min(safe, dist[nr][nc])
                    heapq.heappush(max_heap, (-new_safe, nr, nc))
        
        return 0