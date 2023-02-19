import itertools
a="abb"
list_result=[]
for s in itertools.permutations(a):
    list_result.append(''.join(s))
print(sorted(list(set(list_result))))
