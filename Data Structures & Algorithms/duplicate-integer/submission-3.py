class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory = set()
        for num in nums:
            if num in memory:
                return True
            else:
                memory.add(num)
        return False

        