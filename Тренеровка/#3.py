S = "a=12;c=64;res=a+b;print(res)"

s = S.strip()
s = s.replace("=", " = ")
s = s.replace("+", ' + ')
s = s.replace("*", " * ")
s = s.replace("/", " / ")

a = []
while s.find(";") != -1:
    a += [s[0:s.find(";")]]
    s = s[s.find(";") + 1:]
a += [s[:]]

for i in a:
    print(i)
