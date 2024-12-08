def is_safe_variation(nums: list[int]) -> bool:
    diff = [a-b for a, b in zip(nums, nums[1:])]
    return all(1 <= x <= 3 for  x in diff) or all(-1>= x >= -3 for x in diff)

def is_safe_variation_with_module(nums: list[int]) -> bool:
    return any(is_safe_variation(nums[:index] + nums[index+1:]) for index in range(len(nums)))

with open('./in.txt', 'r') as f:
    input_list = list(list(map(int, i.split())) for i in f.readlines())
    
    print(sum(is_safe_variation_with_module(i) for i in input_list))
