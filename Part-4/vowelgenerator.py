def voweliterator(st1):
    for i in st1:
        if i in 'aeiouAEIOU':
            yield i

ans = voweliterator('abcde')
print(next(ans))
print(next(ans))