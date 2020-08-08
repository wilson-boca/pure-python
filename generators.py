def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


my_nums = square_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(my_nums)


def square_gen(nums):
    for i in nums:
        yield (i*i)


my_nums2 = square_gen([1, 2, 3, 4, 5])
print(my_nums2)

print(next(my_nums2))
print(next(my_nums2))
print(next(my_nums2))
print(next(my_nums2))
print(next(my_nums2))

for num in my_nums2:
    print(num)

# List comprehension
my_nums3 = [x*x for x in [1, 2, 3, 4, 5]]
print(my_nums3)

# Generator
my_nums4 = (x*x for x in [1, 2, 3, 4, 5])
print(list(my_nums4))
