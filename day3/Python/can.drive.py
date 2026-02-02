age = int(input("How old are you? "))
if age >= 18:
    print("You can drive.") 
elif age >= 15:
    print("You can drive with a learner's permit.")
    print("You must be accompanied by a licensed driver.")
    print("You cannot drive yet.")
elif age < 0:
    print("Invalid age entered. Please enter a valid age.")
else:
    print("You cannot drive yet, you little shit!")