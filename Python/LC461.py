class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        c = 0     
        z = x^y
        while (z != 0):
            if z & 1:
                c = c + 1
            z = z >> 1

        return c
            
#---------------------------
a = Solution()
assert a.hammingDistance(1, 4) == 2
assert a.hammingDistance(3, 1) == 1


