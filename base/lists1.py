nums = [10, 20, 30, 50]

print(
    type(nums),
    id(nums),
    nums,
    sep='\n',
    end='\n\n'
)

nums[1] = 2000

print(
    id(nums),
    nums,
    sep='\n',
    end='\n\n'
)

nums.append(60)

print(
    id(nums),
    nums,
    sep='\n',
    end='\n\n'
)

nums.insert(3, 40)

print(
    id(nums),
    nums,
    sep='\n',
    end='\n\n'
)
