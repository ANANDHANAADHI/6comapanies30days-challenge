class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0, 0
        dic1, result = {}, 0

        while right < len(fruits): 
            dic1[fruits[right]] = right
            if len(dic1) >= 3: 
                minVal = min(dic1.values())
                del dic1[fruits[minVal]]
                left = minVal + 1
            result = max(result, right - left + 1)
            right += 1
        return result

        