class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # Step 1: Assign each node to a group/island
        group = [0] * n
        current_group = 0
        
        for i in range(1, n):
            # If the gap between consecutive elements is too big, start a new group
            if nums[i] - nums[i - 1] > maxDiff:
                current_group += 1
            group[i] = current_group
            
        # Step 2: Answer the queries instantly using the group IDs
        answer = []
        for u, v in queries:
            if group[u] == group[v]:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer