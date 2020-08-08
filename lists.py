# Python 4 Interview
# When use a tuple or list?
# A tuple is immutable whereas a list is mutable.
# Tuples are faster than lists.
# If you're defining a constant set of values and all you're ever going to
# do with it is iterate through it, use a tuple instead of a list.
# Dictionary compehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)

# Python set()
# Set has all unique values, ex: nums[1,1,2,3,4,5,5,5,6], my_set = set(nums), result [1,2,3,4,5,6]
# The same as:
nums = [1, 1, 2, 3, 4, 5, 5, 5, 6]
my_set = set(nums)
print(my_set)
my_set2 = {n for n in nums}
print(my_set2)

# using zip() and * operator to
# perform Unzipping
zipped = [("a", 1), ("b", 2)]
unzipped_object = zip(*zipped)
unzipped_list = list(unzipped_object)
print(unzipped_list)

test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
res = list(zip(*test_list))
print(res)
