# bug_bounty.py

def faulty_celsius_to_fahrenheit(celsius):
    # Intended formula: F = C * (9/5) + 32
    # BUG: Incorrect grouping in the formula.
    # The code below uses wrong parentheses so that instead of computing (9/5), it computes 9/(5+32).
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

def run_conversion():
    try:
        user_input = input("Enter temperature in Celsius: ")
        celsius = float(user_input)
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    result = faulty_celsius_to_fahrenheit(celsius)
    print(f"{celsius}° Celsius is {result:.2f}° Fahrenheit")

if __name__ == "__main__":
    run_conversion()
