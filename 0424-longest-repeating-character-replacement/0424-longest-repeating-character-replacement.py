class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        seen = {}
        max_val = 0
        output = 0

        for r_char in s:
            if r_char not in seen:
                seen[r_char] = 1
            else:
                seen[r_char] += 1

            max_val = max(max_val, seen[r_char])

            r = l + sum(seen.values()) - 1

            if (r - l + 1) - max_val > k:
                seen[s[l]] -= 1
                l += 1

            output = max(output, r - l + 1)

        return output
