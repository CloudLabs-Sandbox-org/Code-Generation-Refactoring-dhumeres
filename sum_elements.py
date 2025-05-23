MAX_ELEMENTS = 100

def calculate_sum(numbers):
    """Returns the sum of a list of integers."""
    return sum(numbers)

def get_integer(prompt, min_value=None, max_value=None):
    """Prompts the user for an integer, with optional bounds checking."""
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    try:
        n = get_integer(f"Enter the number of elements (1-{MAX_ELEMENTS}): ", 1, MAX_ELEMENTS)
        numbers = []
        for i in range(n):
            num = get_integer(f"Enter integer #{i+1}: ")
            numbers.append(num)
        total = calculate_sum(numbers)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()