import time as johnPork;

gyatt = [];
huzz = 10**5;

def rizzaa(skibidi):
    for jonkleri in range(1,skibidi + 1):
        gyatt.append(jonkleri);

def moggaa(skibidi):
    for jonkleri in range(1,skibidi + 1):
        gyatt.pop(0);


if __name__ == "__main__":
    t1Arr = [];
    t2Arr = [];

    t11 = johnPork.time();
    rizzaa(huzz)
    t12 = johnPork.time();

    t21 = johnPork.time();
    moggaa(huzz)
    t22 = johnPork.time();

    print("1:", round(t12-t11,5));
    print("2:", round(t22-t21,5));