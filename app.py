# Adding comments for easy understanding and clarity
# Refactoring for the code to be more robust, user-friendly, and maintainable

# UPDATED FUNCTION
# Use *args for variable length arguments
def mean_of_group(*nums):   # Consistency in naming: Python's PEP 8 suggests using snake_case
    if not nums:
        raise ValueError("No numbers provided to calculate mean.")  # Handle incorrect input
    return sum(nums) / len(nums)

# UPDATED FUNCTION
def median_of_group(*nums):
    sorted_nums = sorted(nums)  # sort the sampled numbers
    length = len(sorted_nums)   # count the length (currently, will always be 5)
    return sorted_nums[length // 2]

# UPDATED PROCESSING
# MAIN LOOP
def process_choice(choice, nums):
    if choice == 'mean':
        return mean_of_group(*nums)
    elif choice == 'median':
        return median_of_group(*nums)
    else:
        raise ValueError("Invalid choice. Chose 'mean' or 'median'.")

# Initialize variable that represents the user's choice of operation
choice = ''

# Get five numbers from the user and handle invalid input
def get_nums():
    nums = []
    while len(nums) < 5:
        try:
            num = int(input(f"Enter number {len(nums) + 1}:"))
            nums.append(num)
        except ValueError:
            print("That's not a valid number. Please try again.")
    return nums

nums = get_nums()

# Try and catch block processes the users choice and handles errors 
while True:
    choice = input("Please choose 'mean' or 'median' for your results: ").lower()
    try:
        result = process_choice(choice, nums)
        print(f"Your result is: {result}")
        break
    except ValueError as e:
        print(e)