class Solution:
    # To find a longest prefix in the given string
    # In this Question we have to find longest substring that must be equal to prefix as same as suffix
    def longestPrefix(self, s):
        n = len(s)
        lps= [0]*n
        i = 1;l = 0
        lps[l] =0 
        while(i<n):
            if s[i] == s[l]:
                l+=1
                lps[i] = l
                i+=1
            else:
                if l !=0:
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i+=1
        if lps[-1] == 0:
            return ""
        return s[:lps[-1]] 
s = Solution()
print(s.longestPrefix(input()))