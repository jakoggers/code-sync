class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the middle, left, and right endpoints
        # split the list in half
        # search either left or right, and return the value , else return -1
    
        # Fixed solution: (w/ some neetcode help)

        left, right = 0, len(nums) - 1 # init the right endpoint to the end of nums and left to the start

        while left <= right:
            middle = left + ((right - left) // 2)

            # set the bounds
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1

        '''
        Explaination:
        Summary - Keep moving the bounds until the middle equals the target
        - Set the left equal to the start, and the right equal to the last value of the array: (subtract one so that you know it is at the last value of the array)
        - While left is less than right and doesn't equal right:
            - Find the middle: to prevent overflow, add the left to the (right-left) // 2
            - if the middle is less than the right, the left will equal the middle + 1
            - if the middle is greater than the left, the right will be equal to the middle - 1 
                - both increments/decrements to the numbers find the correct bounds for the left/right
            - otherwise, they're equal, and in that case return the middle
        - if the number wasn't found, then return -1, as the problem states.

        '''
        # Attempt 1:
        '''
        left, right = 0, len(nums)
        left_value, right_value = nums[left], nums[right]
        result = 0

        while left <= right:
            middle = (right - left) // 2
            if target < right_value:
                right_value = nums[right]

            elif target > left_value:
                left = nums[1]
                result = middle
            else: 
                return nums[middle]
        return result
        '''