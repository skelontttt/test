# 读取原始答案字符串（带空格，读一整行）
s = input()
# 构造初始显示列表：字符串不可变，用list方便修改
show = []
for ch in s:
    if ch == ' ':
        show.append(' ')
    else:
        show.append('*')
# 输出初始状态
print(''.join(show))
n = int(input())
for _ in range(n):
    guess = input()  # 每次猜测，读完整一行
    if len(guess) == 1:
        # 开字母操作
        c = guess
        for i in range(len(s)):
            if s[i] == c:
                show[i] = c
        # 输出当前显示串
        print(''.join(show))
    else:
        # 猜测整串，判断Yes/No
        if guess == s:
            print("Yes")
        else:
            print("No")
