#4.（39）[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
import numpy as np
a = [[1,2],[3,4],[5,6]]

#利用array将数组转化为矩阵后，flatten将多维数组转化为一维数组
b = np.array(a).flatten().tolist()
print(b)
