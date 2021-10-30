from gradeCompute import gradeCompute
import numpy

class grade2Compute(gradeCompute):
    def generate(self):
        sign=['+','-','*','/']
        sign_index1 = numpy.random.randint(0, 4)#第一个运算符下标
        sign_index2 = numpy.random.randint(0, 4)#第二个运算符下标
        sign_index3 = numpy.random.randint(0, 4)#第三个运算符下标
        num1 = numpy.random.randint(0,10001)
        num2 = numpy.random.randint(0,10001)
        num3 = numpy.random.randint(0,10001)
        num4 = numpy.random.randint(0,10001)
        opt = numpy.random.randint(0,3)
        form = numpy.random.randint(0,2)
        if opt == 0:
            str1 = str(num1) + ' ' + sign[sign_index1] + ' ' + str(num2) # 生成便于表达式计算的字符串
        elif opt == 1:
            if form == 0:
                str1 = str(num1) + ' ' + sign[sign_index1] + ' ' + str(num2) + ' ' + sign[sign_index2] + ' ' + str(num3)
            else:
                form1 = numpy.random.randint(0,2)
                if form1 == 0:
                    str1 = '(' + str(num1) + ' ' + sign[sign_index1] + ' ' + str(num2) + ')' + ' ' + sign[sign_index2] + ' ' + str(num3)
                else:
                    str1 = str(num1) + ' ' + sign[sign_index1] + ' ' + '(' + str(num2) + ' ' + sign[sign_index2] + ' ' + str(num3) + ')'
        else:
            if form == 0:
                str1 = str(num1) + ' ' + sign[sign_index1] + ' ' + str(num2) + ' ' + sign[sign_index2] + ' ' + str(num3) + ' ' + sign[sign_index3] + ' ' +str(num4)
            else:
                form2 = numpy.random.randint(0,5)
                if form2 == 0:
                    str1 = '(' + str(num1) + ' ' + sign[sign_index1] + ' ' + str(num2) + ')' + ' ' + sign[sign_index2] + ' ' + str(
                        num3) + ' ' + sign[sign_index3] + ' ' + str(num4)
                elif form2 == 1:
                    str1 = '(' + str(num1) + ' ' + sign[sign_index1] + ' ' + str(num2) + ' ' + sign[sign_index2] + ' ' + str(
                        num3) + ')' + ' ' + sign[sign_index3] + ' ' + str(num4)
                elif form2 == 2:
                    str1 = str(num1) + ' ' + sign[sign_index1] + ' ' + '(' + str(num2) + ' ' + sign[sign_index2] + ' ' + str(
                        num3) + ')' + ' ' + sign[sign_index3] + ' ' + str(num4)
                elif form2 == 3:
                    str1 = str(num1) + ' ' + sign[sign_index1] + ' ' + '(' + str(num2) + ' ' + sign[sign_index2] + ' ' + str(
                        num3) + ' ' + sign[sign_index3] + ' ' + str(num4) + ')'
                else:
                    str1 = str(num1) + ' ' + sign[sign_index1] + ' ' + str(num2) + ' ' + sign[sign_index2] + ' ' + '(' + str(
                        num3) + ' ' + sign[sign_index3] + ' ' + str(num4) + ')'
        print(str1 + ' =' + '\n')
        ans = eval(str1)  # 计算表达式
        print(ans)
        return str1

