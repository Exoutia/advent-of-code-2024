import re

def string_to_multiply(a: str) -> int:
    x, y = re.findall(r'\d+', a)
    return int(x) * int(y)

with open('./in.txt', 'r') as f:
    string = f.read()
    matches = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don't\(\)", string)
    skip = False
    ans = 0
    for i in matches:
        if i == "don't()":
            skip = True
        elif i == "do()":
            skip = False
        else:
            if skip:
                continue
            ans += string_to_multiply(i)

    print(ans)

            
        

    
    
