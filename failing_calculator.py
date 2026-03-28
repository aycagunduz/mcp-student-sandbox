def average_ratios(numbers):
    total = 0
    count = 0
    for num in numbers:
        if num != 0:
            total += 100 / num
            count += 1
    if count == 0:
        return 0  # Avoid division by zero if all numbers are zero
    return total / count

print(average_ratios([10, 5, 0]))
