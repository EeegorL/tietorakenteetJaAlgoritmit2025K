# import time;

def find_segments(data):
    current = data[0];
    currentAmount = 0;

    arr = [];
    i = 0;
    for i in range(len(data)):
        this = data[i];

        if(this == current):
            currentAmount += 1;
        else:
            arr.append((currentAmount, current));
            current = this;
            currentAmount = 1;
    arr.append((currentAmount, current));  # appends last (or the only) that wasn't added during loop

    return arr;
     

if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]

    # t1 = time.time();
    # for x in range(1, 100000):
    #     find_segments("aaabbccdddd")
    #     find_segments("aaaaaaaaaaaaaaaaaaaa")
    #     find_segments("abcabc")
    #     find_segments("kissa")
    # t2 = time.time();
    # print(round(t2-t1,2))