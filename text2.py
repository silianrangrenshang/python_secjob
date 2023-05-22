#2.（22）s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"

# 使用 set 对 s 去重并排序
unique_chars = sorted(set(s))

# 过滤掉不需要的字符
filtered_chars = filter(lambda x: x in "adfjl", unique_chars)

# 将结果转换成字符串并输出
result = "".join(filtered_chars)
print(result)
