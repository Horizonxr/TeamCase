import time
import random
from gradeCompute import gradeCompute
sgn = ['-', '+']
class grade1compute(gradeCompute):
    def fun1(self):
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
        return ans

    def fun2(self):
        sig = ['+', '-']
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        num3 = random.randint(0, 100)
        op1 = sig[random.randint(0, 1)]
        op2 = sig[random.randint(0, 1)]
        str1 = str(num1) + op1 + '(' + str(num2) + op2 + str(num3) + ')'
        print(str1)
        ans = eval(str1)
        return ans

    def generate(self):
        choose = random.randint(0, 1)
        if choose == 0:
            return self.fun1()
        elif choose == 1:
            return self.fun2()




