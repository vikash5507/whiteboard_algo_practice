"""

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false


Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].

"""

'''
Solution:
    1. find each subset sum = total/k
    2. sort the nums
    3. 2 pointers l=0, r=size-1 and move both pointers to find subsets possible or not
'''
# nums = [4,3,2,3,5,2,1]
# k = 4

# nums = [1,2,3,4]
# k = 3

# nums = [1,1,1,1,2,2,2,2]
# k = 2

# nums = [1,1,1,1,2,2,2,2]
# k = 3

nums = [4, 4, 6, 2, 3, 8, 10, 2, 10, 7]
k = 4

subset_sum = sum(nums) // k
size = len(nums)
nums.sort()
print(nums, subset_sum)

picked = [False] * size


def can_partition(curr_sum, k, nxt_idx):
    if k == 1:
        return True

    if curr_sum == subset_sum:
        return can_partition(0, k - 1, 0)

    for i in range(nxt_idx, size):
        if not picked[i] and curr_sum + nums[i] <= subset_sum:
            picked[i] = True
            if can_partition(curr_sum + nums[i], k, i+1):
                return True
            picked[i] = False #backtrack

    return False


print(can_partition(0, k, 0))
