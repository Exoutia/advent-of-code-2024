with open('./in.txt', 'r') as f:
    input_list = [map(int, i.split()) for i in f.readlines()]
    list_a, list_b = zip(*input_list)
    list_a = sorted(list_a)
    list_b = sorted(list_b)
    ans = sum(abs(a - b) for a, b in zip(list_a, list_b))
    print(ans)
    
    
