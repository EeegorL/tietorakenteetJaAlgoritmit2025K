def count_rounds(numbers):
    l = len(numbers);
    indexes = [-1] *(l+1);
    for i, n in enumerate(numbers): # jokaista n kohti numberseissa, lisätään sitä vastaava indeksi listaan
        indexes[n] = i;
    print(numbers)
    print(indexes[1:])

    count = 1;
    for i in range(1, l):
        if(indexes[i] > indexes[i+1]): # jos tätä indeksiä seuraava indeksi oli tätä ennen, eli jos menee seuraavalle kierrokselle
            count+=1;

    return count;

"""
    Aina jos nykyindeksi on nykyistä suurempi, niin myöskään sitä seuraavat eivät pääse mukaan kuin vasta jollakin seuraavalla, esim jos 1,2,3,5,4,6,7,8,
    niin stoppaa 5:een koska 5>4, eikä seuraavia voida siten ottaa perään
"""
    
if __name__ == "__main__":
    # print(count_rounds([1, 2, 3, 4])) # 1
    # print(count_rounds([1, 3, 2, 4])) # 2
    # print(count_rounds([4, 3, 2, 1])) # 4
    # print(count_rounds([1])) # 1
    print(count_rounds([1,3,2,4,5,7,6,9,8])) # 4

    # n = 10**5
    # numbers = list(reversed(range(1, n+1)))
    # print(count_rounds(numbers)) # 100000