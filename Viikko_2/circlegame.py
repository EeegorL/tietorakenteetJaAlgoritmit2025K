def find_order(n):
    pelaajat = list(range(1, n+1));
    arr = [];
    i = 0;
    while pelaajat:
        i = ((i+1) % len(pelaajat));
        arr.append(pelaajat.pop(i));
    
    return arr;

if __name__ == "__main__":
    print(find_order(1)) # [1]
    print(find_order(2)) # [2, 1]
    print(find_order(3)) # [2, 1, 3]
    print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]

    order = find_order(10**5)
    print(order[-5:]) # [52545, 85313, 36161, 3393, 68929]

    # def find_order(n):
    # players = list(range(1, n+1))

    # removed = []
    # remove_next = False

    # for player in players:
    #     if remove_next:
    #         removed.append(player)
    #     else:
    #         players.append(player)
    #     remove_next = not remove_next

    # return removed