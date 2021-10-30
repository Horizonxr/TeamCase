#函数负责读入年级，题目数量并返回结果
def IO():
    nianji = input('请输入你的年级?\n')
    while(1):
        problem_num = input('请输入题目数?\n')
        if not problem_num.isnumeric():
            print('非法输入，请检查题目数是否正确')
            continue;
        if '一' in nianji or '二' in nianji:
            nianji_num = 1
        elif '三' in nianji or '四' in nianji:
            nianji_num = 2
        elif '五' in nianji or '六' in nianji:
            nianjiNum = 3
        print(nianji_num)
        print(problem_num)
        break;
    return nianji_num, problem_num
IO()