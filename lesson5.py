# Task 1
# import random
#
# num_size = 10
# numbers = []
# min_number = -10
# max_number = 10
#
# countNegative = 0
# countPair = 0
# countUnpair = 0
# countIndex = 1
# countMaxMinmulti = 1
#
#
# for i in range(num_size):
#     numbers.append(random.randint(min_number, max_number))
# print(numbers)
# MinimumN = min(numbers)
# MaximumN = max(numbers)
# MinimumN_index = numbers.index(MinimumN)
# MaximumN_index = numbers.index(MaximumN)
#
# for i in range(len(numbers)):
#     if numbers[i] < 0:
#         countNegative += numbers[i]
#     if numbers[i] % 2 == 0:
#         countPair += numbers[i]
#     if numbers[i] % 2 != 0:
#         countUnpair += numbers[i]
#     if i % 3 == 0:
#         print(numbers[i])
#         countIndex *= numbers[i]
#     if MaximumN > numbers[i] > MinimumN:
#         countMaxMinmulti *= numbers[i]
#
# print(countNegative)
# print(countPair)
# print(countUnpair)
# print(countIndex)
# print(countMaxMinmulti)



# Task 2
# import random
#
# num_size = 10
# numbers = []
# numbers_1 = []
# numbers_2 = []
# numbers_3 = []
# numbers_4 = []
# min_number = -10
# max_number = 10
#
# for i in range(num_size):
#     numbers.append(random.randint(min_number, max_number))
# print(numbers)
#
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         numbers_1.append(numbers[i])
#     if numbers[i] % 2 != 0:
#         numbers_2.append(numbers[i])
#     if numbers[i] < 0:
#         numbers_3.append(numbers[i])
#     if numbers[i] > 0:
#         numbers_4.append(numbers[i])
#
# print(numbers_1)
# print(numbers_2)
# print(numbers_3)
# print(numbers_4)
