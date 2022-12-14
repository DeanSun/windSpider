# 题目4：请写出一个函数，当输入函数变量当月利润I，能返回应发放奖金总数，例如输出“利润100000元时，应发放奖金总数为10000元。”。
# 其中，企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成
import numbers

I = int(input('请输入当前利润值(万元)：'))
profit = 0
if I <= 10000:
    profit = I
    print(f'I <= 10000:{profit}')
if 100000 < I < 200000:
    profit = profit + (I - 10000) * 0.1
    print(f'100000 < I < 200000:{profit}')
if 200000 <= I < 400000:
    profit = profit + (I - 200000) * 0.75
    print(f'100000 < I < 200000:{profit}')
if 400000 <= I < 600000:
    profit = profit + (I - 400000) * 0.5
    print(f'400000 <= I < 600000:{profit}')
if 600000 <= I < 1000000:
    profit = profit + (I - 600000) * 0.15
    print(f'600000 <= I < 1000000:{profit}')
if I >= 1000000:
    profit = profit + (I - 1000000) * 0.1
    print(f'I >= 1000000:{profit}')
print(profit)
