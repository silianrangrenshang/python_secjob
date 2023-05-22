#5.（52）list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
list = [2,3,5,4,9,6]
sorted_list = []

#解析中使用最小值，则我反之使用最大值进行排序
def get_max(list):
    n = len(list)
    if len(list)>0:

        # 取出最大值元素a
        a = max(list)
        list.remove(a)

        # 添加进入新列表
        get_max(list)
        sorted_list.insert(n,a)

get_max(list)
print(sorted_list)


