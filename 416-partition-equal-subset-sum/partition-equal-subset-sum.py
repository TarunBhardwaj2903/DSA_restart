class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         s=sum(nums)
#         if s % 2 !=0:
#             return False 
#         target = s//2
#         def solve(idx,curr_sum):
#             if curr_sum == target:
#                 return True
#             if idx == len(nums) or curr_sum > target:
#                 return False
#             take = solve(idx+1,curr_sum)
#             not_take = solve(idx+1,curr_sum+nums[idx])

#             return take or not_take
#         return solve(0,0)


