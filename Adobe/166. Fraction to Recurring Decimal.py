class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        

        if numerator == 0:
            return '0'
        

        res = ''
        

        if (numerator > 0 and denominator < 0) or \
            (numerator < 0 and denominator > 0):
            res += '-'
        

        numerator, denominator = abs(numerator), abs(denominator)
        

        res += str(numerator//denominator)
        numerator %= denominator
        if numerator == 0:
            return res
        
        res += '.'
        
        hashmap = {}
        hashmap[numerator] = len(res)
        while numerator != 0:
            
            numerator *= 10
            res += str(numerator//denominator)
            numerator %= denominator
            
            if numerator in hashmap:
                index = hashmap[numerator]
                res = res[:index] + '(' + res[index:]
                res += ')'
                break
            else:
                hashmap[numerator] = len(res)
                 
        return res