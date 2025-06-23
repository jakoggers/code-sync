class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary search method: (w/ neetcode's help)
        l, r = 0, x
        result = 0

        while l <= r:
            middle = l + ((r - l) // 2) # so it doesn't overflow, where it does w/ the parentheses
            if middle**2 > x:
                r = middle - 1
            elif middle**2 < x:
                l = middle + 1
                result = middle
            else:
                return middle
        return result

        # me attempting to explain the solution:
        '''
        - set pointers at the left and right (beginning and end), while setting a result variable
        - while left is less than or equal to right, meaning that until the pointers reach each other, keep performing the next set of operations
        # the value for the middle is set by adding the left to the parentheses value of the right - 1 // 2, finding the middle within the bounds to keep it from over flowing
            - using the squared value (which makes complete sense since they are opposite of the exponent LMAO): compare it to x
                - if the middle squared is greater than the value to be squared:
                    - decrement that value of r, making it so that the right gets smaller and smaller
                - if the middle squared is less than the value to be sqaured:
                    - increment the value of the left, making it so the left gets larget and larger
                    - then, set the result to middle, as it might be the correct value
                - if it reaches the point where both values are equal, return the middle
            - if the left is not greater than right (accounting for the 0 case) return the result
        '''


        # My original attempt:
        '''
        # check if number is prime
            # if prime -> ??
        # obviously check the 0 base case
        if x == 0:
            return 0
        # Given every case:

        # make a list the size of the number that we want to be squared (all 0 for now)
        size_arr = [0] * x
        for i in range(len(size_arr)):
            size_arr[i] = i + 1
        # i loops through, until we hit the last number
        # 'count' counts the number of values until it eqauls the current odd number, where IF we don't hit the last number, we iterate upwards + 2
        square_root = 1
        count = 1
        current_odd = 3
        for i in range(1, len(size_arr) + 1):
            print(f"I: {i}")
            if i == current_odd:
                current_odd += 2
                count = 1
                square_root += 1
            count += 1 # increment
            print(f"Count: {count}")
            print(f"Current odd: {current_odd}")
            print(f"Current square root: {square_root}")

        return square_root

        sqrt:
        Result -> 1: 3 - number of occurances in the following numbers
            - check if current iteration is odd.
            - add each iteration to a list, and return the biggest number in the list
        1 -> 1
        2 -> 1
        3 -> 1
        2: 5
        4 -> 2
        5 -> 2
        6 -> 2
        7 -> 2
        8 -> 2
        3: 7
        9 -> 3
        10 -> 3
        11 -> 3
        12 -> 3
        13 -> 3
        14 -> 3
        15 -> 3
        4: 9
        16 -> 4
        17 -> 4
        18 -> 4
        19 -> 4
        20 -> 4
        21 -> 4
        22 -> 4
        23 -> 4
        24 -> 4
        25 -> 5
        

        # odd numbers are added multiple 
        #  each time it passes a perfect square, the odd number becomes the next one, every given odd number is how many subsequential numbers
        # using the given hint, you can sort them.
        # leetcode lockin by jaykoggers

        '''