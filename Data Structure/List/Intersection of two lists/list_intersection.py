# Program to intersect two list

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
  K = []
  for i in nums1:
    if i in nums2:
      K.append(i)
  return set(K)

