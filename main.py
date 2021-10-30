from problemIO import IO
from grade1Compute import grade1compute
from grade2Compute import grade2Compute
from grade56Compute import grade56Compute

if __name__ == "__main__":
    userInfo = IO()
    grade = int(userInfo[0])
    num = int(userInfo[1])
    wrong = 0
    if grade == 1:
        grade12 = grade1compute()
        for i in range(num):
            true_ans = grade12.generate()
            grade12.ans = true_ans
            user_ans = int(input())
            if not grade12.userAns(user_ans):
                wrong += 1

    elif grade == 2:
        grade34 = grade2Compute()
        for i in range(num):
            true_ans = grade34.generate()
            grade34.ans = true_ans
            user_ans = int(input())
            if not grade34.userAns(user_ans):
                wrong += 1
    elif grade == 3:
        grade56 = grade56Compute()
        for i in range(num):
            true_ans = grade56.generate()
            grade56.ans = true_ans
            user_ans = float(input())
            if not grade56.userAns(user_ans):
                wrong += 1
    if wrong == 0:
        print("结束！全部正确，太棒了！")
    else:
        print("结束！错了"+str(wrong)+"题哦")
