from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = deque([(start, 0)])
        while q:
            g, d = q.popleft()
            if g == end:
                return d
            nb = []
            for cg in bank:
                if sum(i != j for i, j in zip(cg, g)) == 1:
                    q.append((cg, d + 1))  # type: ignore
                else:
                    nb.append(cg)
            bank = nb
        return -1
