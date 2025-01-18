def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage with an empty list which causes ZeroDivisionError
my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

#Improved version
def calculate_average_improved(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
my_numbers = []
average = calculate_average_improved(my_numbers)
print(f"The improved average is: {average}") #This will return 0 instead of error