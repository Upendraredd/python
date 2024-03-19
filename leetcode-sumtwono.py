class Solution(object):
    def twoSum(self, nums, target):
        
        empty_list = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    empty_list.append(i)
                    empty_list.append(j)

        return empty_list
