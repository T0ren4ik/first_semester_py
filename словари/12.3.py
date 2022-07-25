st = "aabbtrg"
el = set(st)

count = {}
for i in el:
    count.update({str(i): st.count(i)})

print(count)
