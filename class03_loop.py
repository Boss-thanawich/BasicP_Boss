# sum = 0
# n = 3

# for i in range(n):
#     sum += i+1

# print(sum)

# for i in range(10):
#     if (i % 2) == 0:
#         print("Even number: ",i)

#-----------------------------------------------

# x = int(input("แม่สูตรคูณ: "))

# for i in range(12):
#     print(x,"*",i+1,"=",x*(i+1))

#-----------------------------------------------

# i = 0 

# while i < 5:
#     print("Hello")
#     i += 1
#     if i == 3:
#         break

#-------------------------------------------------

start = True
while start:
    print("เลือกข้อที่ต้องการเล่น")
    print("ข้อที่ [1]")
    print("ข้อที่ [2]")
    x = int(input("กรุณากรอกเลข: "))
    if (x == 1):
        print("โจทย์ 1")
    elif(x == 2):
        print("โจทย์ 2")
    start = False   
        