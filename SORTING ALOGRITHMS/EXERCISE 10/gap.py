# Maximum Gap

# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra space.

 

# Example 1:

# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
# Example 2:

# Input: nums = [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
 

# Constraints:

# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9




class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bucket sort
        if len(nums) < 2:
            return 0
        max_num = max(nums)
        min_num = min(nums)
        if max_num == min_num:
            return 0
        bucket_size = (max_num - min_num) // (len(nums) - 1)
        if bucket_size == 0:
            bucket_size = 1
        bucket_num = (max_num - min_num) // bucket_size + 1
        buckets = [[] for _ in range(bucket_num)]
        for num in nums:
            buckets[(num - min_num) // bucket_size].append(num)
        buckets = [bucket for bucket in buckets if bucket]
        max_gap = 0
        for i in range(len(buckets) - 1):
            max_gap = max(max_gap, min(buckets[i + 1]) - max(buckets[i]))
        return max_gap
