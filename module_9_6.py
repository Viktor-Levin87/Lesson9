def all_variants(text):
    n = len(text)
    for j in range(1, n + 1):
        for k in range(n - j + 1):
            c = k + j
            yield text[k:c]


a = all_variants("abc")
for i in a:
    print(i)
