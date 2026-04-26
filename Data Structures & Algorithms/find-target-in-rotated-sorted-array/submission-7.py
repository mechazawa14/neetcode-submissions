class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        left ,right = 0, len(nums)-1
        while left< right :
            mid  = (left+right)//2  
            if (nums[mid]> nums[right]):
                left = mid+1
            else:   
                right = mid 
            # by this point wkt at left we have our rotation point 
            # or the partition point 
            #basically left comes out as  our partition point(index) for 2 sorted arrays 
        # Determine which half to search in
        if target >= nums[left] and target <= nums[-1]:
            l, r = left, len(nums) - 1
        else:
            l, r = 0, left - 1

        # Perform binary search
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
