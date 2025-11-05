def find_max_number(num1, num2, num3):
    pass  # Replace 'pass' with code
    if num1 > num2 and num3:
        return (num1)
    elif num2 > num3:
        return (num2)
    else:
        return (num3)
num1 = 1
num2 = 3
num3 = -1
max_num = find_max_number(num1, num2, num3)
print("The maximum number is:", max_num)

def find_mean(num1, num2, num3):
    pass  # Replace 'pass' with code
    n = 3
    sum = num1 + num2 + num3
    return (sum / n)
num1 = 1
num2 = 3
num3 = 2
mean_value = find_mean(num1, num2, num3)
print("The mean is:", mean_value)

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    pass  # Replace 'pass' with code
    n = 3
    sum = num1 + num2 + num3
    sum2 = (sum - num1) ** 2 + (sum - num2) ** 2 + (sum - num3) ** 2
    sum3 = (sum2/n) ** 0.5
    return (mean , sum3)
num1 = 1
num2 = 3
num3 = 2
mean, std = find_mean_std(num1, num2, num3)
print("The mean is", mean)
print("The standard deviation is", std)
