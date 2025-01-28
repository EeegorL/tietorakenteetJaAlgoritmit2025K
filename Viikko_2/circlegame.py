def find_order(n):
    pelaajat = list(range(1, n+1));
    arr = [];
    i = 1;



    while(len(pelaajat) > 0):
        if(i > len(pelaajat)):
            i = len(pelaajat) - 2
        arr.append(pelaajat[i]);
        print(i, pelaajat, pelaajat[i])
        pelaajat.remove(i);
        i+=1;
    return arr;



if __name__ == "__main__":
    order = find_order(4)
    print(order)