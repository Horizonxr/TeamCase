import random


class newgrade56Compute:
    def compute():
        sig = ['+', '-', '*', '/']
        count = random.randint(2, 10)
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
        #如3+5+6*8   左括号插入位置只能是偶数  右括号插入位置只能是奇数  并且相差必须大于等于3小于lenth（str1）
        while 1:
            begin=random.randint(0,count)
            end=random.randint(begin+1,count)
            if (end-begin-3)<=0 and begin%2==0 and  end%2!=0 and end-begin<len(str1):
                break
        #插入空格
        str1.insert(begin,'(')
        str1.insert(end,')')
        ans = eval(str1)
        ans = round(ans, 2)
        return ans
