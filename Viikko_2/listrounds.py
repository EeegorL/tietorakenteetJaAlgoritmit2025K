def find_rounds(numbers):
    allNums = [];
    while(len(numbers) != 0):
        theseNums = [];
        i=0;
        while i < len(numbers):
            m = min(numbers);
            num = numbers[i]
            if num == m:
                theseNums.append(num);
                numbers.remove(num);
            else:
                i+=1;

        allNums.append(theseNums);
    
    return allNums

if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]

    print(find_rounds(list(reversed(range(1, 10**5+1)))))