is_new_century = {
    False: lambda n: n % 4 == 0,
    True: lambda n: n % 400 == 0
}
is_leap = lambda n: is_new_century[n % 100 == 0](n)