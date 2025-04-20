from random import (
    seed, 
    randrange as rr,
    choice,
    sample
)


# seed(2)

nums1 = [rr(10, 100) for _ in range(10)]
print(nums1, end='\n\n')

nums2 = list(range(1, 10))
print(choice(nums2), choice(nums2), choice(nums2), end='\n\n')

print(sample(nums2, 18), end='\n\n')

