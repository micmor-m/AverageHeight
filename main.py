# Average Height
# A program that calculates the average student height from a List of heights.

# Get user input
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Calculate average
total = 0
elements = 0
for value in student_heights:
    total += int(value)
    elements += 1

print(round(total / elements))
