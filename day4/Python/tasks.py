# Define a list of tasks
tasks = ["wake up", "code", "guitar", "eat", "sleep"]

# Using a for loop to iterate through the list
print("For loop with item names:")
for task in tasks:
    print(f"Task: {task}")
    if task == "code":
        print("Time to write some code!")
    elif task == "guitar":
        print("Let's play some music!")
    elif task == "eat":
        print("Don't forget to have a meal!")
    elif task == "sleep":
        print("Rest well for tomorrow!")
    else:
        print("Keep going with your tasks!")

# Using a for loop with index
print("\nFor loop with index:")
for i in range(len(tasks)):
    # range(len(tasks)) gives 0 to len-1
    print(f"Task {i+1}: {tasks[i]}")

print("\nFor loop with counter")
# Using a while loop
count = 0
while count < len(task):
    print("While loop task:", tasks[count])
    count += 1 #don't forget to increment the counter


# Bonus: breaks and continues
print("\nBreak Examples:")
for task in tasks:
    if task == "eat":
        break
    print("Did you:", task)

print("\nContinue example:")
for task in tasks:
    if task == "code":
        continue
    print("Did you:", task)

# Uncomment the code below to try a user-interactive while loop
while True:
    response = input("Type something (or 'quit'): ")
    if response.lower() == "quit":
        break
print("You typed:", response)