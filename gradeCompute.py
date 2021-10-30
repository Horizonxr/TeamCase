#父类

class gradeCompute:
    ans = 0  # 正确答案

    def generate(self):  # 生成表达式，返回表达式，将正确答案存入ans
        return 0

    def userAns(self, user_ans):  # 验证结果，返回正误
        if(self.ans == user_ans):
            return True
        else:
            return False
