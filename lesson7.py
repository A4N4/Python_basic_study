# Task 1
# import random
#
#
# def create_list_numbers(list_length=10, startN=1, endN=10) -> list:
#     numbers_listed = []
#     for i in range(list_length):
#         numbers_listed.append(random.randint(startN, endN))
#     return numbers_listed
#
#
# numbers = create_list_numbers()
# numbers2 = create_list_numbers()
# print(numbers)
# print(numbers2)


# def multiplyN(numbers):
#     multiplyNumbers = 1
#     for i in range(len(numbers)):
#         multiplyNumbers *= numbers[i]
#     return multiplyNumbers
#
#
# numbers_Multiplied = multiplyN(numbers)
# print(numbers_Multiplied)


# Task 2
# def minimum_number(numbers):
#     for i in range(len(numbers)):
#         number_Minimum = min(numbers)
#     return number_Minimum
#
#
# minimum_from_the_list = minimum_number(numbers)
# print(minimum_from_the_list)


# Task 3
# def simple_digit(numbers):
#     count_simple = 0
#     for i in range(len(numbers)):
#         if numbers[i] % 2 != 0:
#             count_simple += 1
#     return count_simple
#
#
# count_simple_from_the_list = simple_digit(numbers)
# print(count_simple_from_the_list)

# Task 4
# Тут у меня не получилось, есть пару черновых вариантов, но они походу неправильные
# v1
# def elements_deleted(list, itemsToDelete):
#     # element_to_delete = int(input("Enter number to delete from 1 to 10: "))
#     count_deleted = 0
#     for i in range(len(list)):
#         if itemsToDelete == list:
#             del(list, i)
#             print(list)
#     # print(list)
#     return (count_deleted)
#
# element_to_delete = int(input("Enter number to delete from 1 to 10: "))
# numbers_deleted_count=elements_deleted(numbers, element_to_delete)
# print(numbers_deleted_count)

# v2
# def delete_items(numbers):
#     for i in range(len(numbers)):
#         if numbers == element_to_delete:
#             remove.numbers[i]
#             count_deleted=0
#             count_deleted+=element_to_delete
#     return(numbers)
#
# element_to_delete = input("Enter element to delete from one to ten: ")
# show_deleted=delete_items(numbers)
# print(show_deleted)

# Task 5
# def same_numbers_in_lists(num1, num2):
#     return (set(num1).intersection(set(num2)))
#
# new_list=same_numbers_in_lists(numbers, numbers2)
# print(new_list)

# Task 6
# Если убрать принт из функции, то ретерн возвращает только один элемент. Можете объяснить почему? И как испавить?

# def num_exponent(list, power):
#     result = 1
#     for i in range(len(list)):
#         result = list[i]**power
#         # print(result, end=" ")
#     return (list[i]**power)
#
#
#
# new_result=num_exponent(numbers,3)
# print(new_result)

