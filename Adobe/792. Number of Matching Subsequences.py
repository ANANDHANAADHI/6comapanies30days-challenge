class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        # 1. word count
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        # 2. check subsequence / string.find method
        def is_subsequence(s, word):
            i = 0
            for char in word:
                i = s.find(char, i) + 1 # s.find(char, i) in s[i:], return -1
                if not i:
                    return False
            return True
        
        # 3. count and return
        res = 0
        for word in word_count:
            if is_subsequence(s, word):
                res += word_count[word]
        return res