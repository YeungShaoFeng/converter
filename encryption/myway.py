class Tre:
    def __init__(self, num, numType):
        self.num = num
        self.numType = numType
        self.treNum, self.bus = 0, 0
        self.go, self.cnt = 3, 0
        self.aM3, self.aD3 = 0, 1
        self.tree, self.Tree = [None] * 100, [None] * 100
        #self.dict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    def GO(self):
        # dec <--> tre
        def TRE(self):
            def tre(self):
                for i in range(len(self.num)):
                    self.bus += int(self.num[0-i-1]) * 10 ** i
                while(self.aD3):
                    self.aM3 = self.bus % self.go
                    self.aD3 = self.bus // self.go
                    self.bus = self.aD3
                    self.tree[self.cnt] = self.aM3
                    self.cnt += 1
                    # print(f"num: {self.bus:02}\t aM3: {self.aM3}\t aD3:\t{self.aD3}")
                #reverse the 0's and 1's
                cnt = 0
                for i in range(self.cnt, -1, -1):
                    if (self.tree[i] != None):
                        self.Tree[cnt] = self.tree[i]
                        cnt += 1
                #creat the treimal number        
                for i in range(self.cnt):
                    self.treNum += self.tree[i] * 10 ** i

                #print the treimal number
                print(f"dec --> tre: {self.treNum}", end='')
                print()
                
            def untre(self):
                for i in range(self.cnt):
                    self.bus += self.tree[i] * 3 ** i
                print("tre --> dec: ", end='')
                print(self.bus)
            # encripythion from dec-->tre
            tre(self)
            untre(self)

        if(self.numType == 10):
            TRE(self)

