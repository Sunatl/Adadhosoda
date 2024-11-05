# lis = [1,2,3,4,5,6]
# cnt = -999999
# cnt1 = -9999
# cnt2 = -999




# for i in lis:
#     if cnt2<cnt1:
#         cnt2 = cnt1
#         cnt1=cnt
#         cnt = i
#     elif cnt1<cnt:
#         cnt1 = cnt
#         cnt = i
#     elif cnt < i:
#         cnt = i
# print(cnt,cnt1,cnt2)

  
  
  
# lis = [1,2,-3,4,5,-6]
# cnt = []
# cnt1 = []

# for i in lis:
#     if i > 0:
#         cnt.append(i)
#     elif i < 0:
#         cnt1.append(i)
        
# print(cnt,cnt1)
        
        


# 10
# with open("mains.txt", "r") as file:
#     s = file.readlines()

# with open("mains1.txt", "w") as file:
#     for x, i in enumerate(s,1):
#         file.write(f"{x}:{i}")





# 1        
# a = int(input("-> "))
# f = 1 
# cnt = 1 

# while f <= a:
#     for i in range(cnt):
#         print(f, end=" ")
#         f += 1
#     print()
#     cnt += 1




# 2
# a = int(input("-> "))

# while a != 1:
#     print(a, end=", ")
#     if a % 2 == 0:
#         a //= 2
#     else:
#        a = a * 3 + 1

# print(a) 


# 4
# a = str(input())
# b = {}
# for i in a:
#     if i == " ":
#         continue
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
# print(b)








#  7
# dict1 = {'a': 1, 'b': 3, 'c': 3}
# dict2 = {'a': 2, 'b': 3, 'c': 4}

# dict3 = {}

# for i in dict1.keys():
#     dict3[i] = dict1[i] + dict2.get(i) 

# print(dict3)



# 8
# with open('mains1.txt', 'r') as file:
#     d = file.read()

# s = d.lower().split()

# a = {}

# for i in s:
#     if i in a:
#         a[i] += 1 
#     else:
#         a[i] = 1  
# print(a)


# 9
n = int(input("-> "))

for i in range(1, n + 1):
    a = " " * (n - i)
    for j in range(1, i + 1):
        a += str(j)
    for j in range(i - 1, 0, -1):
        a += str(j)
    print(a) 


for i in range(n - 1, 0, -1):
    a = " " * (n - i)
    for j in range(1, i + 1):
        a += str(j)
    for j in range(i - 1, 0, -1):
        a += str(j)
    print(a) 





# 13
# filename = 'mains1.txt'
# n = 3

# with open(filename, 'r') as file:
#     d = file.readlines() 
# if n <= len(d):
#     lis = d[-n:] 
# else:
#     d

# for i in lis:
#     print(i, end='')  



# 15
# with open('mains1.txt', 'r') as file:
#     d = file.read()

# s = d.lower().split()

# a = {}

# for i in s:
#     if i in a:
#         a[i] += 1 
#     else:
#         a[i] = 1  

# print(a)



# 16
# file = open('mains1.txt', 'r')
# s = file.readlines()
# file.close() 

# lis = []
# for i in s:
#     if i.strip(): 
#         lis.append(i) 

# file = open('mains1.txt', 'w')
# file.writelines(lis) 
# file.close()  










# 18

# file = open('mains.txt', 'r')

# txt = file.read()

# file.close()

# a = len(txt.split())

# print(f"Dar fili shumo {a} prabel hast")



# 19

# dic = {'apple': 10, 'banana': 5, 'cherry': 15}

# keys = list(dic.keys())

# dic1 = {}

# for i in range(len(keys)):
#     for j in range(len(keys) - 1):
#         if dic[keys[j]] > dic[keys[j + 1]]:
#             keys[j], keys[j + 1] = keys[j + 1], keys[j]

# for q in keys:
#     dic1[q] = dic[q]

# print(dic1) 


# 20

# lis = [5, 3, 8, 6, 7]

# for i in range(len(lis)-1):
#     for j in range(len(lis) - 1):
#         if lis[j] > lis[j + 1]:
#             lis[j], lis[j + 1] = lis[j + 1], lis[j]
            
# print(lis)
# for i in range(len(lis)):
#     for j in range(len(lis) - 1):
#         if lis[j] < lis[j + 1]:
#             lis[j], lis[j + 1] = lis[j + 1], lis[j]

# print(lis) 


# a = int(input("-> "))

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f








# cnt2 = 0
# cnts = a 

# while a > 0:
#     cnt1 = a % 10
#     cnt2 += fact(cnt1) 
#     a //= 10  

# if cnt2 == cnts: 
#     print("Yes")
# else:
#     print("No")