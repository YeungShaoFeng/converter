from time import perf_counter
from myway import Tre

t1 = perf_counter()
# num = Tre(255, 10)
# num.three()
fo = 'D:\\data\\python\\decimal.txt'
fi = 'D:\\data\\python\\treimal.txt'

with open(fo, 'r') as f1:
    with open(fi, 'w') as f2:
        for i in range(10000):
            line = f1.readline().strip()
            if (line):
                # print(f"origin is: {line}")
                num = Tre(line, 10)
                num.GO()
                f2.write("%d" %num.treNum)
                f2.write('\n')

# with open(fo, 'r') as f1:
#     for i in range(10000):
#         line = f1.readline()
#         if (line):
#             print(i, end='\t')
#             print(line)
#             i += 1
t2 = perf_counter()
print(f' GO time is: {t2-t1} s. ')
