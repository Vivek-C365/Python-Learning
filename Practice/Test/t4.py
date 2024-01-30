str = 'this the'
val = {}
for i in str:
    if i in val:
        val[i] += 1
        # print(f"character -- {i} -- occured {val[i]} times")
    else:
        val[i] = 1
        # print(f"character -- {i} -- occured {val[i]} times")

print(val)