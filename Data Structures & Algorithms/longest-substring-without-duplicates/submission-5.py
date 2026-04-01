class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        sub = []
        for c in s:
            if c not in seen:
                seen.append(c)
            else:
                sub.append(len(seen))
                while c in seen:
                    seen.pop(0)
                seen.append(c)
        sub.append(len(seen))
        return max(sub)