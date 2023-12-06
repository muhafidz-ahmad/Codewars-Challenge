def sum_pairs(ints, s):
    seen = set()
    for num in ints:
        target = s - num
        if target in seen:
            return [target, num]
        seen.add(num)
    return None