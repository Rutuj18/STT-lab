"""
Module for solution of 3 Sum problem
"""
def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Finds the unique triplets from given array of numbers having sum zero
    input: A list of numbers 
    output: A list contanining triplets having sum zero
    """
    result = set()
    neg, pos = [],[]
    for x in nums:
        if x > 0:
            pos.append(x)
        elif x < 0:
            neg.append(x)  
    neg_set,pos_set = set(neg),set(pos)
    if 0 in nums:
        result.update({(-x,0,x) for x in pos if -x in neg_set})
        if nums.count(0) >= 3:
            result.add((0,0,0))        
    for i, num1 in enumerate(neg):
        for num2 in neg[i+1]:
            complement = -1 * (num1 + num2)
            if complement in pos_set:
                result.add(tuple(sorted([num1,num2,complement])))               
    for i, num1 in enumerate(pos):
        for num2 in pos[i+1]:
            complement = -1 * (num1 + num2)
            if complement in neg_set:
                result.add(tuple(sorted([num1,num2,complement])))
    return result
