print(*sorted(input(), key=lambda k: (k.isdigit(), k.isdigit() and int(k)%2==0, k.isupper(), k)), sep="")
