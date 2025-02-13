def find_distances(street):
    shops = [];
    distances = [];

    for i, b in enumerate(street):
        if(b == "1"):
            shops.append(i);
    shops = sorted(shops);
    
    for i, house in enumerate(street):
        if(house == 1): # the building itself is a shop
            distances.append(0);
            continue;
        dist = abs(i-shops[0]);
        for s in shops:

            dist = min(abs(i-shops[0]), dist);
        distances.append(dist);
    return distances






if __name__ == "__main__":
    print(find_distances("00100010")) # [2, 1, 0, 1, 2, 1, 0, 1]
    print(find_distances("00100000")) # [2, 1, 0, 1, 2, 3, 4, 5]
    print(find_distances("11111111")) # [0, 0, 0, 0, 0, 0, 0, 0]
    print(find_distances("01010101")) # [1, 0, 1, 0, 1, 0, 1, 0]
    print(find_distances("10000000")) # [0, 1, 2, 3, 4, 5, 6, 7]
    print(find_distances("00000001")) # [7, 6, 5, 4, 3, 2, 1, 0]

    n = 10**5
    street = "0"*n + "1" + "0"*n
    distances = find_distances(street)
    print(distances[1337]) # 98663