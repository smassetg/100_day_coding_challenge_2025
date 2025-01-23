# bug_bounty.py


# bug_bounty.py

# string_reverse_debug.py

#This was the corrected code after debugging
def reverse_string(s):
    reversed_s = ""
    for i in range(len(s) -1, -1, -1):
        reversed_s += s[i]
        print(reversed_s)
    return reversed_s

def main():
    original = "Python"
    reversed_version = reverse_string(original)
    print(f"Original: {original}")
    print(f"Reversed: {reversed_version}")

if __name__ == "__main__":
    main()


#This was the original code
# def reverse_string(s):
#     reversed_s = ""
#     for i in range(len(s)):
#         reversed_s += s[i]
#         print(reversed_s)
#     return reversed_s
#
# def main():
#     original = "Python"
#     reversed_version = reverse_string(original)
#     print(f"Original: {original}")
#     print(f"Reversed: {reversed_version}")
#
# if __name__ == "__main__":
#     main()


# # list_sum_debug.py
# #This is the buggy code, I was practicing with the debugger which is a little confusing
# def sum_list(numbers):
#     total = 0
#     for i in range(len(numbers)):
#         total += numbers[i + 1]
#     return total
#
# def main():
#     numbers = [1, 2, 3, 4, 5]
#     result = sum_list(numbers)
#     print(f"The sum of the list is: {result}")
#
# if __name__ == "__main__":
#     main()


# # list_sum_debug.py, this is the correct code. but it figured this out myself with out th debugger.
# def sum_list(numbers):
#     total = 0
#     for i in range(len(numbers)):
#         total += numbers[i]
#     return total
#
# def main():
#     numbers = [1, 2, 3, 4, 5]
#     result = sum_list(numbers)
#     print(f"The sum of the list is: {result}")
#
# if __name__ == "__main__":
#     main()


# What does this function do?
# if __name__ == "__main__":
#     run_conversion()

# def run_conversion():
#     try:
#         user_input = input("Enter temperature in Celsius: ")
#         celsius = float(user_input)
#     except ValueError:
#         print("Invalid input! Please enter a numeric value.")
#         return