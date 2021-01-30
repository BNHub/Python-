#FIRST VARIANT
# for num in range(1, 101):
#     if num % 3 == 0:
#         if num % 5 == 0:
#             print("FizzBizz")
#             continue
#         print("Fizz")
#         continue
#     if num % 5 == 0:
#         print("Buzz")
#         continue
#     print(num)


# VTORI VARIANT
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBizz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)