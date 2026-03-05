# Example 1:
#
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]


# Example 2:
#
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]

# Constraints:
#
# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000


from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [*nums, *nums]
        return ans


if __name__ == "__main__":
    nums = [1, 2, 1]

    solution = Solution()
    print(solution.getConcatenation(nums))
