class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        total = []
        while l < r:
            if heights[l] > heights[r]:
                height = min(heights[l], heights[r])
                length = r - l
                cont = height * length
                total.append(cont)
                r -= 1
            elif heights[l] < heights[r]:
                height = min(heights[l], heights[r])
                length = r - l
                cont = height * length
                total.append(cont)
                l += 1
            elif heights[l] == heights[r]:
                height = min(heights[l], heights[r])
                length = r - l
                cont = height * length
                total.append(cont)
                l += 1
        return sorted(total, reverse=True)[0]

        