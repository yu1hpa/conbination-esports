import itertools
import os
import random
from contextlib import redirect_stdout

print("空白区切りでメンバーの名前を入力")
member = list(input().strip().split())
out = []

for mem in itertools.combinations_with_replacement(member, 2):
    if(mem[0] == mem[1]):
        with redirect_stdout(open(os.devnull, 'w')):
            print()
    else:
        out.append(mem)

for i in range(len(out)):
    print(random.choice(out))
