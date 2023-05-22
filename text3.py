#3.（36）写一段自定义异常代码
def singular(n):
    try:
        if n <= 0:
            raise Exception('输入小于0了！')
    except Exception as wrong:
        print(wrong)

n = int(input('输入一个大于0的数：'))
singular(n)