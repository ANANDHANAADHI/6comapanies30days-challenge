class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        N = len(nums[0])
        is_trimmed = [False] * N
        trims = [[] for _ in range(N)]
                
        ans = []
        for k, trim in queries:
            if not is_trimmed[trim-1]:
				# we perform the sort only if the relevant trim size is queried and save it for multiple queries
                is_trimmed[trim-1] = True
                trims[trim-1] = sorted([(int(n[-trim:]), i) for i, n in enumerate(nums)])
            ans.append(trims[trim-1][k-1][-1])
            
        return ans