def xo(s):
    count_x = s.lower().count("x")
    count_o = s.lower().count("o")
    if count_x == count_o:
        return True
    return False