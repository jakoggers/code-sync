class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        new_list = []
        # loop through
        nums.sort()
        for i in range(len(nums) - 1):
            check_first = nums[i]
            if check_first == nums[i + 1]:
                new_list.append(check_first)
        return new_list