with open('in.txt', 'r') as f:
    string = f.read().splitlines()
    rules, updates = string[:string.index('')], string[string.index('')+1:]
    updates = [i.split(',') for i in updates]

    rules = set(rules)


    def following_rules(nums: list[str]) -> tuple[bool, int, int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[j] + '|' + nums[i]) in rules:
                    return False, i, j
        return True, -1, -1

    def fixed_update(nums: list[str]) -> bool:
        if following_rules(nums)[0]:
            return False
        while True:
            following_rules_var, i, j = following_rules(nums)
            if following_rules_var:
                return True
            nums[i], nums[j] = nums[j], nums[i]

    ans = 0
    
    for update in updates:
        if fixed_update(update):
            ans += int(update[len(update) // 2])
    print(ans)

            

            
        
        
    
