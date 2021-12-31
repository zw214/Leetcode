class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if (not nums or len(nums) < 3):
            return []
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return ans
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i]+nums[left]+nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i]+nums[left]+nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return ans
