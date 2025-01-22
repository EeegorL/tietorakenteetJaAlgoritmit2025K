def count_numbers(a, b):
    res = 0;
    # 2 5 22 25 52 55
    # 222 225 252 255
    # 522 525 552 555
    # 2222 2225 2252 2255 2522 2552 2555 2525
    # 5555 5552 5525 5522 5255 5225 5222 5252

    return res;
        

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    # print(count_numbers(1, 10**9)) # 1022
    # print(count_numbers(123456789, 987654321)) # 512