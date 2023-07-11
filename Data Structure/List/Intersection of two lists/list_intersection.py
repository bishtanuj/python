# Program to intersect two list

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
  K = []
  for i in nums1:
    if i in nums2:
      K.append(i)
  return set(K)


if __name__ == "__main__":
  nums1 = list(map(int, input("Enter the elements of Array 1: ").split()))
  nums2 = list(map(int, input("Enter the elements of Array 2: ").split()))
  print(f"Intersection: {intersect(nums1, nums2)}")


'''
OUTPUT:
'''
