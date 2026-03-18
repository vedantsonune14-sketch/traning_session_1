# 1.Two Sum

# class Solution:
#     def twoSum(self, nums, target):
#         mp = {}

#         for i in range(len(nums)):
#             remaining = target - nums[i]

#             if remaining in mp:
#                 return [mp[remaining], i]

#             mp[nums[i]] = i


# 2.Fizz Buzz

# class Solution: 
#     def fizzBuzz(self, n: int) -> List[str]:
#         result = []

#         for i in range(1, n + 1):
#             if i % 15 == 0:
#                 result.append("FizzBuzz")
#             elif i % 3 == 0:
#                 result.append("Fizz")
#             elif i % 5 == 0:
#                 result.append("Buzz")
#             else:
#                 result.append(str(i))

#         return result

# 3.running-sum-of-1d-array
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         running_sum = 0
#         result = []

#         for num in nums:
#             running_sum += num
#             result.append(running_sum)

#         return result

# 4.n = 4
# array = [1, 3, 2, 4]
# output = find_next_larger_elements(array)
# print(output)

def find_next_larger_elements(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result