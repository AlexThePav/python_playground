# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:
#
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:
#
# Input: nums = [1,0,1,1,0,1]
# Output: 2

# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_total = 0
        running_total = 0
        for i in nums:
            if i == 1:
                running_total += 1
                if running_total > max_total:
                    max_total = running_total
            else:
                running_total = 0
        return max_total


if __name__ == "__main__":
    nums = [1,1,0,1,1,1]

    solution = Solution()
    print(solution.findMaxConsecutiveOnes(nums))

