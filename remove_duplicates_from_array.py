from typing import List


def removeDuplicates(nums: List[int]) -> int:
    pointer1 = 0
    for pointer2 in range(1, len(nums), 1):
        if nums[pointer1] is not nums[pointer2]:
            pointer1 += 1
            nums[pointer1] = nums[pointer2]
    return pointer1 + 1


def build_my_solution():
    nums = [-50, -50, -49, -48, -47, -47, -47, -46, -45, -43, -42, -41, -40, -40, -40, -40, -40, -40, -39, -38, -38, -38,
         -38, -37, -36, -35, -34, -34, -34, -33, -32, -31, -30, -28, -27, -26, -26, -26, -25, -25, -24, -24, -24, -22,
         -22, -21, -21, -21, -21, -21, -20, -19, -18, -18, -18, -17, -17, -17, -17, -17, -16, -16, -15, -14, -14, -14,
         -13, -13, -12, -12, -10, -10, -9, -8, -8, -7, -7, -6, -5, -4, -3, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
         13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 25, 26, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44,
         45, 46, 47, 48, 49, 50]
    removeDuplicates(nums)
    print(nums)


if __name__ == '__main__':
    build_my_solution()
