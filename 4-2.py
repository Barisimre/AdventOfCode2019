count = 0
for i in range(246540,787419):
    st = str(i)
    double = False
    # Increasing
    works = sorted(st) == list(st)
    # One pair
    for i in range(len(st) - 3):
        if st[i] < st[i+1] and st[i+1] == st[i+2] and st[i+2] < st[i+3] and i in range(len(st) - 2):
            double = True
    if st[0] == st[1] and st[1] != st[2] or st[-1] == st[-2] and st[-3] != st[-2]:
        double = True
    if works and double:
        count += 1
print(count)