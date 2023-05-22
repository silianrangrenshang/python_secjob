#1.（14）python中生成随机整数、随机小数、0--1之间小数方法
import random
"""随机整数"""
ranint = random.randint(1,1000)
print('生成随机整数：',ranint)

"""随机小数"""
ranpoint = random.uniform(0.0,1000.0)
print('生成随机小数：',ranpoint)

"""0-1小数"""
ranzetoone = random.uniform(0.0,1.0)
print('生成随机0-1的小数：',ranzetoone)