import random


class gradeCompute
    ans = 0  # 正确答案

    def __init__(self, ans)
        self.ans = ans

    def generate(self)  # 生成表达式，返回表达式，将正确答案存入ans
        return 0

    def userAns(self, user_ans)  # 验证结果，返回正误
        if(self.ans == user_ans)
            return True
        else
            return False

class grade56Compute(gradeCompute)
    def __init__(self)
        self.sig = ['+', '-', '', '']
    def compute()
        sig = ['+', '-', '', '']
        count = random.randint(2, 5)
        nums = []
        operators = []
        str1 = ''
        for i in range(count)
            nums.append(random.uniform(0, 10001))
            nums[i] = round(nums[i], 2)
        for i in range(count - 1)
            operators.append(sig[random.randint(0, 3)])
        for i in range(count - 1)
            str1 += str(nums[i])
            str1 += operators[i]
        str1 += str(nums[count - 1])
        print(str1)
        # print(nums)
        # print(operators)
        ans = eval(str1)
        ans = round(ans, 2)
        print(ans)


test = grade56Compute
test.compute()

