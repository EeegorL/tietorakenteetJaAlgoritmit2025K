def find_number(numbers):
    num1 = numbers[0];
    num1Count = 0;

    for num in numbers:
        if num == num1:
            num1Count += 1;
        if(num != num1):
            num2 = num;
    
    if(num1Count == 1):
        return num1;
    else:
        return num2;

if __name__ == "__main__":
    print(find_number([1, 1, 1, 2])) # 2
    print(find_number([1, 1, 2, 1])) # 2
    print(find_number([1, 2, 1, 1])) # 2
    print(find_number([2, 1, 1, 1])) # 2
    print(find_number([5, 5, 5, 3, 5])) # 3
    print(find_number([1, 100, 1])) # 100

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers)) # 2