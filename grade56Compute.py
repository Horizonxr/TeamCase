import random


class gradeCompute:
    ans = 0  # 正确答案

    def __init__(self, ans):
        self.ans = ans

    def generate(self):  # 生成表达式，返回表达式，将正确答案存入ans
        return 0

    def userAns(self, user_ans):  # 验证结果，返回正误
        if self.ans == user_ans:
            return True
        else:
            return False


class grade56Compute(gradeCompute):

    def fun1(self):
        sig = ['+', '-', '*', '/']
        count = random.randint(2, 5)
        nums = []
        operators = []
        str1 = ''
        for i in range(count):
            nums.append(random.uniform(0, 10001))
            nums[i] = round(nums[i], 2)
        for i in range(count - 1):
            operators.append(sig[random.randint(0, 3)])
        for i in range(count - 1):
            str1 += str(nums[i])
            str1 += operators[i]
        str1 += str(nums[count - 1])
        print(str1)
        # print(nums)
        # print(operators)
        ans = eval(str1)
        ans = round(ans, 2)
        print(ans)
        return ans

    def fun2(self):
        sig = ['+', '-', '*', '/']
        num1 = round(random.uniform(0, 10000), 2)
        num2 = round(random.uniform(0, 10000), 2)
        num3 = round(random.uniform(0, 10000), 2)
        op1 = sig[random.randint(0, 1)]
        op2 = sig[random.randint(2, 3)]
        str1 = str(num1) + op1 + str(num2)
        ans1 = eval(str1)
        str2 = str(ans1) + op2 + str(num3)
        ans = round(eval(str2), 2)
        str3 = '(' + str1 + ')' + op2 + str(num3)
        print(str3)
        print(ans)
        return ans

    def generate(self):
        choose = random.randint(0, 1)
        if choose == 0:
            self.fun1(self)
        elif choose == 1:
            self.fun2(self)

test = grade56Compute
test.generate(test)

