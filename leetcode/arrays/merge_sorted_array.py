import time
from ch2.generate_numbers import generate_test_data
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

Constraints:
    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1.length == m + n
    nums2.length == n
"""


class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of nums1.
        nums1_copy = nums1[:m]
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2.
        p1 = 0
        p2 = 0

        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

    def merge_aux_space(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if nums1 is None or len(nums1) == 0:
            return nums2
        if nums2 is None or len(nums2) == 0:
            return nums1
        current_m = 0
        current_n = 0
        merged = []
        while current_m < m and current_n < n:
            if nums1[current_m] <= nums2[current_n]:
                merged.append(nums1[current_m])
                current_m += 1
            else:
                merged.append(nums2[current_n])
                current_n += 1

        if current_m < m:
            for i in range(current_m, m):
                merged.append(nums1[i])

        if current_n < n:
            for i in range(current_n, n):
                merged.append(nums2[i])

        return merged


if __name__ == "__main__":
    s = Solution()
    a = [1, 9]
    b = [2, 3]
    print(s.merge_aux_space(a, len(a), b, len(b)))
    assert s.merge_aux_space(a, len(a), b, len(b)) == [1, 2, 3, 9]

    a = [1, 9, 0, 0]
    b = [2, 3]
    s.merge(a, len(a), b, len(b))
    print(a)
    assert s.merge(a, len(a), b, len(b)) == [1, 2, 3, 9]

    a = None
    b = [4, 5, 6, 7]
    print(s.merge_aux_space(a, 0, b, len(b)))
    assert s.merge_aux_space(a, 0, b, len(b)) == [4, 5, 6, 7]

    a = [4, 5, 6, 7]
    b = None
    print(s.merge_aux_space(a, len(a), b, 0))
    assert s.merge_aux_space(a, len(a), b, 0) == [4, 5, 6, 7]

    start = time.time()
    a = generate_test_data(100000)
    b = generate_test_data(500000)
    res = s.merge_aux_space(a, len(a), b, len(b))
    print(f"execution time = {time.time() - start}")
    print(res[:30])
    print(res[-30:])
