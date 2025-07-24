# x = ["Boss","Pee"]
# print(x)

# x[0] = "Gun"
# print(x)

# x.append("Net")
# print(x)

# x.pop(1)
# print(x)

#-------------------------------------------------

# x = ["a","b","c","d"]
# print(len(x))
# #----วิธีที่1--------
# # for i in range(len(x)):
# #     print(x[i])
# #----วิธีที่2--------
# # for name in x:
# #     print(name)

#--------------------------------------------------

# score = [99,10,23,50]
# sum = 0

# for i in range(len(score)):
#     print(sum)
#     sum += score[i]

# print("total:",sum)

#-------------------------------------------------

num = [1,2,3,4,5,6,7,8,9,10]

for number in num :
    if number % 2 == 0:
        print("Even:",number)
    else:
        print("odd:",number)