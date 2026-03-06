# Example 1:
#
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
# Example 2:
#
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
# Example 3:
#
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]

# nums = [2,5,1,3,4,7]
# n = 3
# expected: [2,3,5,4,1,7]

# nums = [7,5,9,7,5,8,10,4,3,3,2,5,9,10]
# n = 7
# expected: [7,4,5,3,9,3,7,2,5,5,8,9,10,10]

# Constraints:
#
# 1 <= n <= 500
# nums.length == 2n
# 1 <= nums[i] <= 10^3
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int] | str:
        final_list = []
        if 1 <= n <= 500:
            for i in range(n):
                final_list.extend(nums[i::n] if 1 <= nums[i] <= 10**3 else None)
        else:
            return "n cosntraint!"

        return final_list


if __name__ == "__main__":
    nums = [2,5,1,3,4,7]
    n = 3

    solution = Solution()
    print(solution.shuffle(nums, n))

