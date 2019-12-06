count = 0
for i in range(246540,787419):
    st = str(i)
    double = False
    # Increasing
    works = sorted(st) == list(st)
    # One pair
    for i in st:
        for j in st[st.index(i)+1:]:
            if i == j:
                double = True

    if works and double:
        count += 1
print(count)