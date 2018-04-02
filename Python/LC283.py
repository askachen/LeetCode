import time

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """ # SOLUTION #1
        # switch w/ next none zero
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                continue
            for j in range (i+1, length):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], 0 # magic!
                    break
        """

        # SOLUTION 2
        i = 0
        length = len(nums)
        while (i < length):
            if nums[i] is 0:
                nums.pop(i)
                nums.append(0)
                length = length - 1
            else:
                i = i + 1
            
        print nums

#---------------------------
a = Solution()
start_time = time.time()
print a.moveZeroes([0, 1, 0, 3, 12])
print a.moveZeroes([0, 0, 1])
print time.time() - start_time
