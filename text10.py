#10.（101）求两个列表的交集、差集、并集
# 定义两个列表
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# 求交集
jiaoji = list(set(list1) & set(list2))
print("交集：", jiaoji)

# 求差集
chaji = list(set(list1) - set(list2))
print("差集：", chaji)

# 求并集
binji = list(set(list1) | set(list2))
print("并集：", binji) 
