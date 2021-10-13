import itertools
import os
from contextlib import redirect_stdout

print("空白区切りでメンバーの名前を入力")
member = list(input().strip().split())

for mem in itertools.combinations_with_replacement(member, 2):
    if(mem[0] == mem[1]):
        with redirect_stdout(open(os.devnull, 'w')):
            print()
    else:
        print(mem)
