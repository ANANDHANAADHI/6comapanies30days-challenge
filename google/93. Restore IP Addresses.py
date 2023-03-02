class Solution:
    res = None

    def add_if_complete_ip(self, ip_addr: str) -> bool:
        if ip_addr.count('.') == 3:
            self.res.add(ip_addr)

    def is_valide_ip(self, ip_addr: str) -> bool:
        if ip_addr.count('.') > 3:
            return False

        for sub_addr in ip_addr.split('.'):
            if len(sub_addr) > 1 and sub_addr[0] == '0':
                return False

            if len(sub_addr) > 0 and int(sub_addr) > 255:
                return False

        return True

    def backtrack(self, index: int, s: str, ip_addr: str):
        if index >= len(s):
            return self.add_if_complete_ip(ip_addr)            

        s_chr = s[index]
        
        ip_addr += s_chr
        if self.is_valide_ip(ip_addr):
            self.backtrack(index+1, s, ip_addr)

        if len(ip_addr) > 1:
            ip_addr = ip_addr[:-1] + f'.{s_chr}'
            if self.is_valide_ip(ip_addr):
                self.backtrack(index+1, s, ip_addr)


    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = set()

        self.backtrack(0, s, '')

        return self.res