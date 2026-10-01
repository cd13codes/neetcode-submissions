class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        final = sorted(set(nums))  # remove duplicates & sort
        k, maxe = 1, 1

        for i in range(len(final) - 1):
            if final[i] + 1 == final[i + 1]:
                k += 1
            else:
                k = 1
            maxe = max(maxe, k)

        return maxe
