def is_safe(nums: list[int]) -> bool:
    is_negative = 0 > nums[0] - nums[1]
    for i in range(len(nums) - 1):
        res = nums[i] - nums[i + 1]
        if ((res < 0) ^ is_negative):
            return False
        if res == 0 or abs(res) > 3:
            return False
    return True
        
        
def is_safe_variation(nums: list[int]) -> bool:
    diff = [a-b for a, b in zip(nums, nums[1:])]
    return all(1 <= x <= 3 for  x in diff) or all(-1>= x >= -3 for x in diff)


with open('./in.txt', 'r') as f:
    input_list = list(list(map(int, i.split())) for i in f.readlines())
    
    print(sum(is_safe(i) for i in input_list))
