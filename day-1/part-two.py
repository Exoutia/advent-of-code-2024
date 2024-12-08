from collections import Counter


with open('./in.txt', 'r') as f:
    input_list = [map(int, i.split()) for i in f.readlines()]
    list_a, list_b = zip(*input_list)
    counter_b = Counter(list_b)

    ans = 0
    for i in list_a:
        if i in counter_b:
            print(i, counter_b[i])
            ans += i * counter_b[i]

    
    print(ans)
    
    
