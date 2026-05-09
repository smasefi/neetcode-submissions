class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        curr = 0
        for i in nums:
            if i == curr:
                return True
            curr = i
        return False
         