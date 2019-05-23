from sys import getsizeof


# ----<binary reading>

# inputfile = 'D:/data/python/bin.bin'
# with open(inputfile, 'rb') as f:
#     for i in range(2):
#         for j in range(4):
#             data = f.read(4)
#             print(data)

# ----</binary reading>

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ----<i's change>

# print("i\ti-a\ta-i\t0-i")
# a = 10
# for i in range(a, -1, -1):
#     print(i, end='\t')
#     print(i-a, end='\t')
#     print(a-i, end='\t')
#     print(0-i)
# print()

# ----<i's change>

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ----<replacement of str>

# a = 'a\u203a'
# b = '\u203a'
# print(type(a))
# if(isinstance(a, str)):
#     print(1)

# if (a.replace(b, '')):
#     print(2)
#     print(a)

# a = a.replace(b, '')

# print(a)

# ----</replacement of str>

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ----<list appends list>

# a = [None, None, 1,22,3,4]
# for i in range(10):
#     a.append([])
#     for j in range(i):
#         a[j].append(j)
#         print(a[i][j])
#     # a[i].append([i])
#     print(a)

# ----</list appends list>

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ----<getsizeof>

# print(getsizeof([]))
# print(getsizeof([0]))
# print(getsizeof([None]))

# ----</getsizeof>

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ----<var in list>

# ls = [1, 2, 3, 4]
# for var in ls:
#     if (var == 2):
#         print(var)
# def fout(ls, var):
#     for j in range(4):
#         if (j>1 and j%var==0):
#             print(" ", end='')
#         print(ls[j], end='')
#     print()

# ls = [1, 2, 3, 4, 16]
# if (isinstance(ls, list)):
#     for var in ls:
#         if (var==2):
#             print("{} convert to Binary is : ".format(ls))
#             fout(ls, 4)
#             # break
#         elif (var==3):
#             print("{} convert to Treimal is : ".format(ls))
#             fout(ls, var)
#             # break
#         elif (var==8):
#             print("{} convert to Octal is : ".format(ls)) 
#             fout(ls, 3)
#             # break
#         elif (var==16):
#             print("{} convert to Hexadecimal is : ".format(ls)) 
#             fout(ls, 4)
#             # break
#         elif (var):
#             print("{} convert to whateveral is : ".format(ls)) 
#             fout(ls, 3)
#             # break 
# ----<var in list>

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ----<str to list>
# s = '123'
s = [1, 2, 3]
# print(int(s))
# print(len(s))
# print(s.replace('\u203a', ''))
# s = list(s)
# print(s)
# print(len(s))
for i in range(len(s)):
    print(int(s[i]))

# ----<str to list>

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ERROR----<i[0][j]>

# a = [1]
# print(a[0][0])

# ----</i[0][j]>

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

