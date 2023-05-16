import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        c  = re.compile('^' + p+'$')
        print(p)
        if c.match(s):
            return True
        else:
            return False