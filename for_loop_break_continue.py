# Define a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Iterate over each number in the list
for num in numbers:
    # Skip the number 3
    if num == 3:
        continue  # Skip this iteration and move to the next number
    
    # Exit the loop if the number is 7
    if num == 7:
        break  # Stop the loop completely

    # Print the current number
    print(num)
