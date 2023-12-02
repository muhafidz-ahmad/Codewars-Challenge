def persistence(n):
    str_value = str(n)
    count = 0
    while len(str_value) > 1:
        value = 1
        for i in str_value:
            value *= int(i)
        str_value = str(value)
        count += 1
    return count