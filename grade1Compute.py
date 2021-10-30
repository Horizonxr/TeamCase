import time
import random
from gradeCompute import gradeCompute
sgn=['-','+']
class grade1compute(gradeCompute):
    def generate():
        sig = ['+', '-'] #加减符号
        count = random.randint(2, 5)#2至5个数的相加减
        nums = []
        operators = []
        str1 = ''
        for i in range(count):#循环加减
            nums.append(random.randint(0, 100))#随机生成0-100之内的数
            nums[i] = round(nums[i], 2)
        for i in range(count - 1):
            operators.append(sig[random.randint(0, 1)])
        for i in range(count - 1):
            str1 += str(nums[i])
            str1 += operators[i]
        str1 += str(nums[count - 1])
        print(str1)
        # print(nums)
        # print(operators)
        ans = eval(str1) #用函数计算简化代码
        ans = round(ans, 2)
        print(ans)

