#函数负责读入年级，题目数量并返回结果
def IO():
    nianji = input('请输入你的年级?\n')
    nianji_num = 0
    problem_num = int(input('请输入题目数?\n'))
    if '一' in nianji or '二' in nianji:
        nianji_num = 1
    elif '三' in nianji or '四' in nianji:
        nianji_num = 2
    elif '五' in nianji or '六' in nianji:
        nianji_num = 3
    return nianji_num, problem_num