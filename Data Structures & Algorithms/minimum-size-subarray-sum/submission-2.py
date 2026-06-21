class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        curSum = 0
        length = float("inf")

        for R in range(len(nums)):
            curSum += nums[R]
            while curSum >= target:
                length = min(R - L + 1, length)
                curSum -= nums[L]
                L += 1

        return 0 if length == float("inf") else length