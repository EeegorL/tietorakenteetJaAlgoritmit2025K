def count_splits(sequence):
    l = len(sequence);
    count = 0;

    if(len(sequence) % 2 != 0):
        return 0;

    i=2;
    while(i < l):
        print(sequence[0:i] + " : " + sequence[i:l]);
        i+=2;
    print("----")
    # return count;
    return;



if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    # sequence = "01"*10**5
    # print(count_splits(sequence)) # 99999