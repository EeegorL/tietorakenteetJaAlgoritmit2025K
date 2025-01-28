def count_rounds(numbers):
    _low = min(numbers);
    _max = max(numbers);

    # tää on nyt niinku itse toiminnallisuus mut miten tätä simulois... pää lyö nimittäin tyhjää
    arrs = [];
    for x in numbers:
        isInSomeArr = False;
        for arr in arrs:
            if(x-1 in arr):
                arr.append(x);
                isInSomeArr = True;
                break;
        if(not isInSomeArr):
            arrs.append([x]);

    return len(arrs);
    

if __name__ == "__main__":
    # print(count_rounds([1, 2, 3, 4])) # 1
    # print(count_rounds([1, 3, 2, 4])) # 2
    # print(count_rounds([4, 3, 2, 1])) # 4
    # print(count_rounds([1])) # 1
    # print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000
    ...