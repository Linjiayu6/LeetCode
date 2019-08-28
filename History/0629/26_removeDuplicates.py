
# def removeDuplicates(nums):
#   i = len(nums) - 1
#   while(i > 0):
#     D = nums[i]
#     while(True):
#       j = i - 1
#       if (nums[j] == D):
#         del nums[j]
#         i -= 1
#         j -= 1
#       else:
#         break
#     i -= 1
#   return nums
# print(removeDuplicates([1,1,2]))

def removeDuplicates(nums):
  # i = 0, j = 1
  if len(nums) <= 1:
    return len(nums)
  i = 0
  j = i + 1
  while(True):
    if (j >= len(nums)):
      break

    if nums[i] != nums[j]:
      i += 1
      j = i + 1
    else:
      del nums[j]
  return len(nums)

print(removeDuplicates([1,1,2]))