class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # This pointer tracks the position for the next valid element
        
        # Iterate through the array with the 'i' pointer
        for i in range(len(nums)):
            # If the current element is NOT the value we want to remove
            if nums[i] != val:
                # Move it to the front of the array at index 'k'
                nums[k] = nums[i]
                # Increment 'k' to prepare for the next valid element
                k += 1
                
        # Returning 'k' tells LeetCode how many valid elements are left
        return k