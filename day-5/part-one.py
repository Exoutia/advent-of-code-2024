with open('in.txt', 'r') as f:
    string = f.read().splitlines()
    rules, updates = string[:string.index('')], string[string.index('')+1:]
    updates = [i.split(',') for i in updates]

    rules = set(rules)


    def following_rules(nums: list[str]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[j] + '|' + nums[i]) in rules:
                    return False
        return True


    ans = 0
    
    for update in updates:
        if following_rules(update):
            ans += int(update[len(update) // 2])
    print(ans)

            

            
        
        
    
