from sys import getsizeof
from time import perf_counter

class Tre:
    def __init__(self, num, aimtype):
        self.bus = 0
        self.num = num
        self.aimtype = aimtype
        self.treNum, self.cnt = [0], [0]
        self.tree, self.Tree = [[0]], [[0]]

    def GO(self):
        def tre(self, i):
            def step(self, i):
                while(self.bus):
                    self.tree[i][self.cnt[i]] = self.bus % self.aimtype[i]
                    self.bus //= self.aimtype[i]
                    if (self.bus):
                        self.tree[i].append(0)
                        self.Tree[i].append(0)
                    self.cnt[i] += 1
                for j in range(self.cnt[i]-1, -1, -1):
                    self.Tree[i][self.cnt[i]-j-1] = self.tree[i][j]
                    self.treNum[i] += self.tree[i][j] * self.aimtype[i] ** j
            def mapper(self):
                cnt = 0
                for var in self.Tree[i]:
                    if (var == 10):
                        self.Tree[i][cnt] = 'A'
                        cnt += 1
                    elif (var == 11):
                        self.Tree[i][cnt] = 'B'
                        cnt += 1
                    elif (var == 12):
                        self.Tree[i][cnt] = 'C'
                        cnt += 1
                    elif (var == 13):
                        self.Tree[i][cnt] = 'D'
                        cnt += 1
                    elif (var == 14):
                        self.Tree[i][cnt] = 'E'
                        cnt += 1
                    elif (var == 15):
                        self.Tree[i][cnt] = 'F'
                        cnt += 1

            step(self, i)
            if(i < len(self.aimtype)-1):
                self.cnt.append(0)
                self.treNum.append(0)
                self.tree.append([0])
                self.Tree.append([0])
                self.bus = int(self.num)
            if (self.aimtype[i]==16):
                mapper(self)

        def treOut(self, i):
            def fout(self, var):
                for j in range(self.cnt[i]):
                    if (j>1 and j%var==0):
                        print(" ", end='')
                    print(self.Tree[i][j], end='')
                print()
            def judge(self, var):
                if (var==2):
                    print("Bin: ", end='')      # {} convert to  .format(self.num)
                    fout(self, 4)
                elif (var==3):
                    print("Tre: ", end='')
                    fout(self, 3)
                elif (var==8):
                    print("Oct: ", end='') 
                    fout(self, 3)
                elif (var==16):
                    print("Hex: ", end='') 
                    fout(self, 4)
                elif (var):
                    print("Wha: ", end='') 
                    fout(self, 3)
            judge(self, int(self.aimtype[i]))
        # def untre(self):
        #     for i in range(self.cnt):
        #         self.bus += self.tree[i] * 3 ** i
        self.num = self.num.replace("\u202c", '')
        self.bus = int(self.num)
        for i in range(len(self.aimtype)):
            tre(self, i)
            if (not i):
                print("Dec: {}".format(self.num))
            treOut(self, i)


t1 = perf_counter()

# a = '9223372036854775807‬3148789465169745616516987987915321654979'
# a = '255'
b = '4077'
# print(f"sizeof(tre) = {getsizeof(Tre)}")
num = Tre(b, [16, 8, 2])
# print(f"sizeof(num) = {getsizeof(num)}")
num.GO()
# print(f"sizeof(tre) = {getsizeof(Tre)}")
t2 = perf_counter()
print(f'GO time is: {t2-t1} s. ')
