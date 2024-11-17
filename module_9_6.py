def all_variants(text):
    count = len(text)
    step = 0

    for step in range(1, count + 1):
        for i in range(count - step + 1):
            yield text[i:i + step]





a = all_variants("abcd")
for i in a:
    print(i)