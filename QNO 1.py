class Solution(object):
    def twoSum(self, nums, target):
        prevs = {}
        for index,num in enumerate(nums):
            if target - num in prevs:
                return [prevs[target-num],index]
            prevs[num] = index
