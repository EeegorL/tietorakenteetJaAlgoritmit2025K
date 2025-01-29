def count_rounds(numbers):
    l = len(numbers);
    indexes = [-1] *(l+1);
    for i, n in enumerate(numbers): # jokaista n kohti numberseissa, lisätään sitä vastaava indeksi listaan
        indexes[n] = i;

    count = 1;
    for i in range(1, l):
        if(indexes[i+1] < indexes[i]): # jos tätä indeksiä seuraava indeksi oli tätä ennen, eli jos menee seuraavalle kierrokselle
            count+=1;

    return count;
    
if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000