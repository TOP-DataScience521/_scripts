nums1 = [10, 20, 30, 40]
nums2 = nums1

print(id(nums1), id(nums2), sep='\n', end='\n\n')

nums2[2] = 3000

print(nums1, id(nums1))
print(nums2, id(nums2))

