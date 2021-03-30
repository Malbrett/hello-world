def fizzbuzz(maxim):
    for n in range(1, (maxim+1)):
        out = ""
        if n % 3 == 0:
            out += "FIZZ"
        if n % 5 == 0:
            out += "BUZZ"
        if len(out) == 0:
            out = n
        print(out)


fizzbuzz(100)
