def count_sublists(numbers):
    l = len(numbers);
    amount = 0;
    counter = 0;
    prev = -1;
    for i in range(0, l):
        this = numbers[i];
        if(this > prev):
            counter += 1;
        

if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4])) # 7
    print(count_sublists([1, 2, 3, 4])) # 10
    print(count_sublists([4, 3, 2, 1])) # 4
    print(count_sublists([1, 1, 1, 1])) # 4
    print(count_sublists([1, 2, 1, 2])) # 6

    numbers = list(range(1, 10**5+1))
    print(count_sublists(numbers)) # 5000050000