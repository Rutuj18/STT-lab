
def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Finds the unique triplets from given array of numbers having sum zero
    
    input: A list of numbers 
    output: A list contanining triplets having sum zero
    """
    result = set()
    neg, pos, zero = [], [], []
    for x in nums:
        if x > 0:
            pos.append(x)
        elif x < 0:
            neg.append(x)
        else:
            zero.append(x)
    neg_set, pos_set = set(neg), set(pos)

    if zero:
        for x in pos:
            if -x in neg_set:
                result.add((-x, 0, x))
    if len(zero) >= 3:
        result.add((0, 0, 0))

    for i in range(len(neg)):
        for j in range(i + 1, len(neg)):
            complement = -1 * (neg[i] + neg[j])
            if complement in pos_set:
                result.add(tuple(sorted([neg[i], neg[j], complement])))

    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            complement = -1 * (pos[i] + pos[j])
            if complement in neg_set:
                result.add(tuple(sorted([pos[i], pos[j], complement])))
    return result
