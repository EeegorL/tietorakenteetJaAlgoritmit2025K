def count_rounds(numbers):
    def skibidi(arr, x):
        min = 0;
        max = len(arr) - 1;

        while min <= max:
            mid = min + (max - min) // 2;
            print(mid);

            min +=1;

    skibidi(numbers, 1)

if __name__ == "__main__":
    # print(count_rounds([1, 2, 3, 4])) # 1
    count_rounds([1,2,3,4,5,6,7,8,9,10])
    # print(count_rounds([1, 3, 2, 4])) # 2
    # print(count_rounds([4, 3, 2, 1])) # 4
    # print(count_rounds([1])) # 1
    # print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    # n = 10**5
    # numbers = list(reversed(range(1, n+1)))
    # print(count_rounds(numbers)) # 100000