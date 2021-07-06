import itertools

print("空白区切りでメンバーの名前を入力して")
member = list(input().strip().split())

for mem in itertools.permutations(member, 2):
    print(mem)
