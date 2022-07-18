def square_numbers(nums):
    for i in nums:
        yield (i * i)


my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums) #this prints out the generator object's location in memory

print(next(my_nums)) # prints the first value
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums)) # After exhausting the generator it raises StopIteration exception

# To avoid that if u want all the values printed out use a for loop on the generator object
# coz the for loop will stop before StopIteration exception
for num in my_nums:
    print(num)
