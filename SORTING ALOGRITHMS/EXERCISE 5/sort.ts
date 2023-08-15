// Sort Colors

// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

// We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

// You must solve this problem without using the library's sort function.

 

// Example 1:

// Input: nums = [2,0,2,1,1,0]
// Output: [0,0,1,1,2,2]
// Example 2:

// Input: nums = [2,0,1]
// Output: [0,1,2]
 

// Constraints:

// n == nums.length
// 1 <= n <= 300
// nums[i] is either 0, 1, or 2.
 

/**
 Do not return anything, modify nums in-place instead.
 */
 function sortColors(nums: number[]): void {
    let low = 0;       // Index for 0 (red)
    let high = nums.length - 1;  // Index for 2 (blue)
    let current = 0;   // Current index being checked
    
    while (current <= high) {
        if (nums[current] === 0) {
            // If the current element is 0, swap it with the element at the low index
            [nums[current], nums[low]] = [nums[low], nums[current]];
            low++;
            current++;
        } else if (nums[current] === 2) {
            // If the current element is 2, swap it with the element at the high index
            [nums[current], nums[high]] = [nums[high], nums[current]];
            high--;
        } else {
            // If the current element is 1, just move to the next element
            current++;
        }
    }
}