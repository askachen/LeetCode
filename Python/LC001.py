class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)

        my_dict = dict()
        for i in range(0, length):
            compliment = target - nums[i]
            if my_dict.has_key(compliment):
                return [my_dict[compliment], i]
            else:
                my_dict[nums[i]] = i
                #print my_dict

#---------------------------
a = Solution()
print a.twoSum([2, 7, 11, 15], 9)
print a.twoSum([-1,-2,-3,-4,-5], -8)

