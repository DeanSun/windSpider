# 用字典的值对字典进行排序

import operator

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x)
