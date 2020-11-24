a = list(range(1,11,1))
b = a[5:len(a)]
a = list(set(a) - set(b))
c = [0] + list(a) + list(b)
print(sorted(c))