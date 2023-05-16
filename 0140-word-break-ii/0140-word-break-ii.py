class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        def backtrack(current, s,output):
            candidate = "".join(current)
            if candidate == s:
                output.append(" ".join(current))
                return
            elif candidate != s[:len(candidate)]:
                return

            else:
                for word in wordDict:
                    backtrack(current + [word],s,output)

            return output
        return backtrack([],s,[])

            
                