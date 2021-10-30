from gradeCompute import gradeCompute
import numpy


class grade2Compute(gradeCompute):
    def generate(self):
        sign = ['+', '-', '*', '/']
        num = []
        sign_index = []
        lift_brackets = -1
        right_brackets = -1
        str1 = ''
        opt = numpy.random.randint(1, 4)  # 随机生成操作数为2，3，4的情况
        form = numpy.random.randint(0, 2)  # 随机生成有无括号情况
        if form == 1 and opt > 1:
            lift_brackets = numpy.random.randint(0, opt)
            right_brackets = numpy.random.randint(lift_brackets + 1, opt+1)
        i = 0
        while i < opt:
            if i == lift_brackets:
                num += ['(' + str(numpy.random.randint(0, 10001))]  # 将左括号与数字拼接
            elif i == right_brackets:
                num += [str(numpy.random.randint(0, 10001)) + ')']  # 将右括号与数字拼接
            else:
                num += [numpy.random.randint(0, 10001)]
            sign_index += [numpy.random.randint(0, 4)]
            str1 = str1 + str(num[i]) + sign[sign_index[i]]
            i += 1
        str1 += str(numpy.random.randint(0, 10001))
        if right_brackets == opt:
            str1 += ')'
        print(str1)  # 输出算式
        ans = int(eval(str1.replace('/', '//')))
        return ans