def sum_of_divisors(n):
    divisors_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

def classify_number(n):
    divisors_sum = sum_of_divisors(n)

    if divisors_sum == n:
        return "Perfect"
    elif divisors_sum > n:
        return "Abundant"
    else:
        return "Deficient"

number = 30
classification = classify_number(number)
print(f"The number {number} is {classification}.")