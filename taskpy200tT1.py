# Mean, Median, Mode using basic constructs (no inbuilt statistics functions)

# Input list
numbers = [10, 20, 30, 40, 50, 20]

# --------- MEAN ----------
total = 0
count = 0

for num in numbers:
    total = total + num
    count = count + 1

mean = total / count
print("Mean:", mean)


# --------- MEDIAN ----------
# Step 1: Sort manually (Bubble Sort)
sorted_numbers = numbers.copy()

n = len(sorted_numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_numbers[j] > sorted_numbers[j + 1]:
            temp = sorted_numbers[j]
            sorted_numbers[j] = sorted_numbers[j + 1]
            sorted_numbers[j + 1] = temp

# Step 2: Find median
if n % 2 == 0:
    mid1 = sorted_numbers[n // 2]
    mid2 = sorted_numbers[n // 2 - 1]
    median = (mid1 + mid2) / 2
else:
    median = sorted_numbers[n // 2]

print("Median:", median)


# --------- MODE ----------
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1

max_count = 0
mode = None

for key in frequency:
    if frequency[key] > max_count:
        max_count = frequency[key]
        mode = key

print("Mode:", mode)