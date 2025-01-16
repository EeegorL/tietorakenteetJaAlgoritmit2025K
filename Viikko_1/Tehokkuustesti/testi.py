import random;
import time;

def count_even1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

random.seed(1234);
numbers = [round(random.random() * 100) for i in range(10**7)]; # testing with whole numbers just feels better :)

sum1 = 0;
sum2 = 0;
n = 100;

for x in range(n): # run tests n times and get the mean because the values vary
    t1_1 = time.time();
    count_even1(numbers);
    t2_1 = time.time();

    t1_2 = time.time();
    count_even2(numbers);
    t2_2 = time.time();

    sum1 += round(t2_1-t1_1, 2);
    sum2 += round(t2_2-t1_2, 2);

print("1:",round(sum1/n,2));
print("2:",round(sum2/n,2));