# numbers = [10, 11, 12, 13, 14, 15]
# numbers.reverse()
# print("Using reverse() ", numbers)
#
# print("Using reversed() ", list(reversed(numbers)))
#
# print(numbers.reverse())

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_numbers = list(filter(lambda number: number >= 5, numbers))

print(filtered_numbers)
print(numbers)


