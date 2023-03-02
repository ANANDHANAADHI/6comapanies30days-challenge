class Solution:
    def mostPopularCreator(self, creators, ids, views):
        dict1, dict2, result = defaultdict(list), defaultdict(int), []

        for i,j,k in zip(creators,ids,views):
            dict1[i].append((k,j))
            dict2[i] += k

        max_val = max(dict2.values())

        ans = [key for key,val in dict2.items() if val == max_val]

        for i in ans:
            val = sorted(dict1[i], key = lambda x: (-x[0],x[1]))[:1][0]
            result.append([i,val[1]])

        return result

