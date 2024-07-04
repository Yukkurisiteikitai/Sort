Number = [3, 5, 1, 2, 4, 6, 3,3,123,212,432,32]

#a = random.randint(50, 100)
for i in range(1000):
    a = random.randint(1, 1008932)
    Number.append(a)

# 挿入ソートアルゴリズム
for i in range(1, len(Number)):
    key = Number[i]
    j = i - 1
    while j >= 0 and key < Number[j]:
        Number[j + 1] = Number[j]
        j -= 1
    Number[j + 1] = key

# ソートされたリストを表示
for k in Number:
    print(k)
        
