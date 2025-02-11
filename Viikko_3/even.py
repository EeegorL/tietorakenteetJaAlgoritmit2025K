def count_sublists(numbers):
    l = len(numbers);
    counter = 0;

    evenStreak = 0;
    for i in range(0, l):
        if(numbers[i] % 2 == 0):
            evenStreak += 1;
        else:
            counter += int(((evenStreak * (evenStreak + 1)) / 2)); # (n(n + 1) / 2)
            evenStreak = 0;
    
        if(i == (l - 1)):
            counter += int(((evenStreak * (evenStreak + 1)) / 2));

    return counter;


if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6])) # 4
    print(count_sublists([1, 2, 3, 4])) # 2
    print(count_sublists([1, 1, 1, 1])) # 0
    print(count_sublists([2, 2, 2, 2])) # 10
    print(count_sublists([1, 1, 2, 1])) # 1

    numbers = [2] * 10**5
    print(count_sublists(numbers)) # 5000050000