Input=[1, 5.2, 4, 0, -1]
Input2= [-2.398]
def sum_array(numbers):
    if not numbers:  
        return 0

    total = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num

    return total


print(sum_array(Input))
print(sum_array(Input2))