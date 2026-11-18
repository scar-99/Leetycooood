class Solution(object):
    def longestCommonSubsequence(self, text1, text2):

        if len(text1) < len(text2):
            text1,text2 = text2 ,text1 
        m = len(text1)
        n = len(text2)

        prev = [0]*(n + 1)
        curr = [0]*(n + 1)

        for i in range (1, m + 1):
            for j in range(1, n + 1):

                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(curr[j - 1], prev[j])

            prev, curr = curr, prev
        return(prev[n])
