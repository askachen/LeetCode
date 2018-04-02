import time

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """# SOLUTION 1
        nums.sort()
        i = 0
        length = len(nums)
        while (i < length - 1):
            if nums[i] != nums[i+1]:
                return nums[i]
            i = i + 2
        return nums[length - 1]
        """

        # SOLUTION 2
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return s.pop()
        
        """# SOLUTION 3
        return 2 * sum(set(nums)) - sum(nums)
        """

#---------------------------
a = Solution()
start_time = time.time()
print a.singleNumber([2, 1, 7, 1, 3, 2, 7])
print time.time() - start_time
