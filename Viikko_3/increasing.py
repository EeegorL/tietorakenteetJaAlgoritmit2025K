def count_sublists(numbers):
    count = 1; # lasketaan heti ensimmäinen nro
    l = len(numbers);
    streak = 1;

    for i in range(1,l):
        if(numbers[i] > numbers[i-1]): # ei out of bounds koska count alkaa 1stä
            streak += 1;
        else:
            streak = 1;
    
        count += streak;
        
    return int(count);
        

if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4])) # 7
    print(count_sublists([1, 2, 3, 4])) # 10
    print(count_sublists([4, 3, 2, 1])) # 4
    print(count_sublists([1, 1, 1, 1])) # 4
    print(count_sublists([1, 2, 1, 2])) # 6

    numbers = list(range(1, 10**5+1))
    print(count_sublists(numbers)) # 5000050000