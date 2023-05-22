#6.（58）使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
"""使用pop方法"""
dic={"name":"zs","age":18}
dic.pop("name")
print(dic)

"""使用del方法"""
dic={"name":"zs","age":18}
del dic["name"]
print(dic)
