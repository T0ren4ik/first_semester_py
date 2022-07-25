S = "2" + 100 * "7"

newS = S

while newS.find("17") != -1 or newS.find("277") != -1 or newS.find("3777") != -1:
    newS = newS.replace("17", "2", 1)
    newS = newS.replace("277", "3", 1)
    newS = newS.replace("3777", "1", 1)

print(newS)