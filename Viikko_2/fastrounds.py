def count_rounds(numbers):
    _low = min(numbers);
    _max = max(numbers);

    # tää on nyt niinku itse toiminnallisuus mut miten tätä simulois... pää lyö nimittäin tyhjää
    arrs = [];
    for x in numbers:
        isInSomeArr = False;
        for arr in arrs:
            if(x-1 in arr):
                arr.add(x);
                isInSomeArr = True;
                break;
        if(not isInSomeArr):
            s = set(); s.add(x)
            arrs.append(s);
    print(arrs)
    return len(arrs);
    

if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    # n = 10**4
    # numbers = list(reversed(range(1, n+1)))
    # print(count_rounds(numbers)) # 100000
