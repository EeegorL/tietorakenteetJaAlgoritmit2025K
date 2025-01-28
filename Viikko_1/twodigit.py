def count_numbers(a, b):
    # def getNext(num):
    #     if(a <= num <= b):
    #         nonlocal count; # mahdollistaa ei-paikallisen muuttujan käytön
    #         count += 1;
        
    #     if(num > b):
    #         return;
    
    #     getNext(num * 10 + 2);  # jatkaa rekursiivisesti edellisestä luoden 2 uutta laskentahaaraa
    #     getNext(num * 10 + 5);

    # count = 0;
    # getNext(0); # aloittaa kaiken jippiiiii!

    count = 0;
    nums = [2,5];

    for num in nums:
        if(a <= num <= b):
            count+=1;
        if(num > b):
            break;

        nums.append(num * 10 + 2);
        nums.append(num * 10 + 5);

    return count;

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512