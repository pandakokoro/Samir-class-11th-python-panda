import time

# Collect and sanitize user inputs
name = str(input("What is your name: ")).strip().title()
age = int(input("What is your age: "))

# Simulate visual loading progress
for i in range(11):
    print(f"\rProcessing step {i}/10", end="", flush=True)
    time.sleep(0.5)

# Conditional logic for status determination
if age >= 18:
    status = "an adult"
else:
    status = "a minor"

# Final output
print(f"\nBoss, you are {name}, {age} years old, and currently {status}.")
