#7.（72）对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
sorted_foo = sorted(foo,key=lambda x:x)
print(sorted_foo)