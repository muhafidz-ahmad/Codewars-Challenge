# return masked string
def maskify(cc):
    if len(cc) > 4:
        return ("#" * (len(cc) - 4)) + cc[-4:]
    return cc