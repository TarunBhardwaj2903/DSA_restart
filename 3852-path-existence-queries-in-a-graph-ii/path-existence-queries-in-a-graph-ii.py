import math

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Step 1: Track original indices by sorting pairs of (value, original_index)
        sorted_nodes = sorted((val, idx) for idx, val in enumerate(nums))
        
        # Create a map to quickly look up where an original index sits in our sorted list
        sorted_pos = [0] * n
        for sorted_idx, (val, orig_idx) in enumerate(sorted_nodes):
            sorted_pos[orig_idx] = sorted_idx
            
        # Step 2: Determine the maximum binary jump levels needed (e.g., 2^17 > 10^5)
        LOG = math.ceil(math.log2(n)) + 1
        
        # jump[i][j] will store: "farthest sorted index reached from 'i' in 2^j steps"
        jump = [[0] * LOG for _ in range(n)]
        
        # Step 3: Find the farthest 1-hop (2^0 = 1 step) using two pointers
        right = 0
        for left in range(n):
            while right + 1 < n and sorted_nodes[right + 1][0] - sorted_nodes[left][0] <= maxDiff:
                right += 1
            jump[left][0] = right  # Farthest index reachable in 1 hop
            
        # Step 4: Fill the Binary Lifting table
        # "Jumping 2^j steps" is the same as jumping 2^(j-1) steps, and then 2^(j-1) steps from there!
        for j in range(1, LOG):
            for i in range(n):
                intermediate_node = jump[i][j - 1]
                jump[i][j] = jump[intermediate_node][j - 1]
                
        # Step 5: Answer each query
        answer = []
        for u, v in queries:
            # Convert original graph nodes to their positions in our sorted array
            pos_u = sorted_pos[u]
            pos_v = sorted_pos[v]
            
            # Since the graph is undirected, make sure we are traveling left-to-right (from small to large)
            if pos_u > pos_v:
                pos_u, pos_v = pos_v, pos_u
                
            if pos_u == pos_v:
                answer.append(0)
                continue
                
            # Use binary lifting to jump as close to pos_v as possible without crossing it
            curr = pos_u
            steps = 0
            for j in range(LOG - 1, -1, -1):
                if jump[curr][j] < pos_v:
                    curr = jump[curr][j]
                    steps += (1 << j)  # Add 2^j steps to our tally
            
            # We are now standing at 'curr', which is the farthest we can get *before* pos_v.
            # Can we make one final 1-hop to land on or past pos_v?
            if jump[curr][0] >= pos_v:
                answer.append(steps + 1)
            else:
                answer.append(-1)  # A gap blocks us; they are in different components
                
        return answer