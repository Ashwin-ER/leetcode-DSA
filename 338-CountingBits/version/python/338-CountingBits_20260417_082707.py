# Last updated: 17/04/2026, 08:27:07
1class Solution:
2    def countBits(self, n: int) -> list[int]:
3        ans = [0] * (n + 1)
4        for i in range(1, n + 1):
5            # Bit count of i = bit count of (i without last bit) + last bit
6            ans[i] = ans[i >> 1] + (i & 1)
7        return ans