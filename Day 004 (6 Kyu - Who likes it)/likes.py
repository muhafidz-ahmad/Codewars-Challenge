def likes(names):
    total_names = len(names)
    if total_names == 0:
        return "no one likes this"
    elif total_names == 1:
        return names[0] + " likes this"
    elif total_names == 2:
        return names[0] + " and " + names[1] + " like this"
    elif total_names == 3:
        return ", ".join(names[0:2]) + " and " + names[2] + " like this"
    else:
        return ", ".join(names[0:2]) + " and " + str(len(names[2:])) + " others like this"