import time

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #SOLUTION 1
        #return s[::-1]

        #SOLUTION 2
        rs = list("")
        length = len(s)
        for i in range(length):
            rs.append(s[length-i-1])
        return "".join(rs)

#---------------------------
a = Solution()
start_time = time.time()
print a.reverseString("hello")
print a.reverseString("Tesla is accelerating the world's transition to sustainable energy, offering the safest, quickest electric cars on the road and integrated energy solutions. Tesla products work together to power your home and charge your electric car with clean energy, day and night.")
print time.time() - start_time
