class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s = set()
        MorseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            key = ""
            for char in word:
                key += MorseCode[ord(char) - ord('a')]
            s.add(key)

        return len(s)
        
#---------------------------
a = Solution()
print a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
#print a.uniqueMorseRepresentations([1,2])
