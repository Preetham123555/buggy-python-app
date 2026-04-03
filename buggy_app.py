
# Buggy Python App - Has Multiple Bugs!

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num  # Fix: correct augmentation operator
    return total / len(numbers)

# Function to find the index of a target item in a list
def find_item(items, target):
    i = 0
    while i < len(items):
        if items[i] == target:
            return i
        i += 1  # Fix: increment i to avoid infinite loop
    return -1  # Return -1 if item not found

# Function to check if a password is correct
def check_password(password):
    correct = "secret123"
    if password == correct:  # Fix: correct comparison operator
        return True
    return False

# Function to get the last item in a list
def get_last_item(my_list):
    return my_list[len(my_list) - 1]  # Fix: correct index for last item

# Function to greet a user
def greet_user(name, age):
    return f"Hello {name}, you are {age} years old"  # Fix: use f-string for string concatenation

# Main function
def main():
    numbers = [10, 20, 30, 40, 50]
    print(calculate_average(numbers))
    items = ["apple", "banana", "cherry"]
    print(find_item(items, "banana"))
    print(check_password("secret123"))
    print(get_last_item(numbers))
    print(greet_user("John", 25))

if __name__ == "__main__":
    main()
