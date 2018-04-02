import time

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rs = list("")
        for i in range(1, n+1):
            three = True if i % 3 == 0 else False
            five = True if i % 5 == 0 else False
            if three and five:
                rs.append("FizzBuzz")
            elif three:
                rs.append("Fizz")
            elif five:
                rs.append("Buzz")
            else:
                rs.append(str(i))
        return rs


#---------------------------
a = Solution()
start_time = time.time()
print a.fizzBuzz(15)
print a.fizzBuzz(1)
print time.time() - start_time
