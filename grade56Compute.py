import random
from gradeCompute import gradeCompute
class grade56Compute(gradeCompute):
    def __init__(self):
        self.sig = ['+', '-', '*', '/']
    def generate(self):
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
        # print(str1)
        # print(nums)
        # print(operators)
        ans = eval(str1)
        ans = round(ans, 2)
        print(ans)
        return ans

