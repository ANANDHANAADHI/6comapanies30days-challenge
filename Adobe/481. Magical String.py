class Solution:
    def magicalString(self, n: int) -> int:
        if n < 4:
            return 1
        nums = [0] * (n + 1)
        nums[2] = 2
        number2Add = 1
        pos = 2
        cnt = 1

        insertPos = 3
        while insertPos < n:
            for _ in range(nums[pos]):
                nums[insertPos] = number2Add
                insertPos += 1                
            
            if number2Add == 1:
                cnt += nums[pos]                
                number2Add = 2
            else:
                number2Add = 1
            pos += 1

        if nums[-1] == 1:
            cnt -= 1
        return cnt