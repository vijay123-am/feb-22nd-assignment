# def check_number_type(num):
#     if num > 0:
#         print(f"{num} is a positive number.")
#     elif num < 0:
#         print(f"{num} is a negative number.")
#     else:
#         print(f"{num} is zero.")
# print(check_number_type(4))


# def print_even_numbers(limit):
#     print(f"Even numbers up to {limit}:")
#     for i in range(limit + 1):
#         if i % 2 == 0:
#             print(i, end=' ')
#     print()
# print(print_even_numbers(30))


# def sum_natural_numbers(n):
#     sum = 0
#     i = 1
#     while i <= n:
#         sum += i
#         i += 1
#     return sum

# print(sum_natural_numbers(10))  



# def find_number(numbers, target):
#     for num in numbers:
#         if num == target:
#             print(f"Found the number: {target}")
#             break
#     else:
#         print(f"Number {target} not found in the list.")
# print(find_number([1,2,3,4,5],5))


# count = 5
# while count > 0:
#     print(f"Countdown: {count}")
#     count -= 1
# else:
#     print("Liftoff!")


# def reverse_number(num):
#     reversed_num = 0
#     while num > 0:
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit
#         num //= 10
#     return reversed_num

# print(reverse_number(1234)) 