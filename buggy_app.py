# Buggy Python App - Has Multiple Bugs!

# Bug 1: Wrong division operator
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total =+ num  # Bug: should be +=
    return total / len(numbers)

# Bug 2: Infinite loop
def find_item(items, target):
    i = 0
    while i < len(items):
        if items[i] == target:
            return i
        # Bug: i never increments

# Bug 3: Wrong comparison operator
def check_password(password):
    correct = "secret123"
    if password = correct:  # Bug: should be ==
        return True
    return False

# Bug 4: List index out of range
def get_last_item(my_list):
    return my_list[len(my_list)]  # Bug: should be len-1

# Bug 5: String concatenation error
def greet_user(name, age):
    return "Hello " + name + " you are " + age + " years old"

# Main
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
