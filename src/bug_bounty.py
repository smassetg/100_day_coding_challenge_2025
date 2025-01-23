# bug_bounty.py


# bug_bounty.py


# list_sum_debug.py
def sum_list(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

def main():
    numbers = [1, 2, 3, 4, 5]
    result = sum_list(numbers)
    print(f"The sum of the list is: {result}")

if __name__ == "__main__":
    main()


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