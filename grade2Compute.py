from gradeCompute import gradeCompute
import numpy
class grade2Compute(gradeCompute):
    def generate(self):
        sign=['+','-','*','/']
        sign_lindex=numpy.random.randint(0,4)#第一个运算符下标
        sign_rindex=numpy.random.randint(0,4)#第二个运算符下标
        num1=numpy.random.randint(0,10001)
        num2=numpy.random.randint(0,10001)
        num3=numpy.random.randint(0,10001)#三个运算项下标
        str1 = str(num1) + ' ' + sign[sign_lindex] + ' ' + str(num2) + ' ' + sign[sign_rindex] + ' ' + str(
            num3) # 生成便于表达式计算的字符串
        print(str1 + '='+ '\n')
        ans = int(eval(str1))  # 计算表达式
        return str1
